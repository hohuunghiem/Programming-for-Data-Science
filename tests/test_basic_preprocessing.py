"""Small fixtures exercise the actual preprocessing functions in Notebook 01.

Run from the repository root: python -m unittest discover -s tests -v
"""

import ast
import json
import os
from pathlib import Path
import tempfile
import unittest

os.environ.setdefault("MPLBACKEND", "Agg")

import numpy as np
import pandas as pd


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks/01_collection_exploration.ipynb"
CELLS = {
    cell["id"]: "".join(cell["source"])
    for cell in json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]
    if cell["cell_type"] == "code"
}
FUNCTIONS = {}
exec(CELLS["setup-and-loader"], FUNCTIONS)
for tag in ["review-rules", "cleaning-function"]:
    definitions = [
        node for node in ast.parse(CELLS[tag]).body if isinstance(node, ast.FunctionDef)
    ]
    exec(compile(ast.Module(body=definitions, type_ignores=[]), str(NOTEBOOK), "exec"), FUNCTIONS)

load_asteroids = FUNCTIONS["load_asteroids"]
build_review_flags = FUNCTIONS["build_review_flags"]
prepare_shared_data = FUNCTIONS["prepare_shared_data"]


def fixture():
    table = pd.DataFrame({col: [1.0, 2.0, 3.0] for col in FUNCTIONS["COLUMN_INFO"]})
    for col in FUNCTIONS["TEXT_COLUMNS"]:
        table[col] = pd.Series(["example"] * 3, dtype="string")
    table["id"] = pd.Series(["0001", "0002", "0003"], dtype="string")
    table["spkid"] = pd.Series(["00101", "00102", "00103"], dtype="string")
    table["full_name"] = pd.Series(["  Name  A  ", pd.NA, "NA"], dtype="string")
    table["neo"] = pd.Series(["N", "Y", pd.NA], dtype="string")
    table["pha"] = pd.Series(["N", pd.NA, "Y"], dtype="string")
    table["class"] = pd.Series(["MBA", "HYA", "TNO"], dtype="string")
    table["e"] = [0.1, 1.8, 0.3]
    table["a"] = [2.5, -6.0, 30.0]
    table["albedo"] = [0.1, np.nan, 1.2]
    return table


class BasicPreprocessingTests(unittest.TestCase):
    def test_loader_preserves_identifiers_and_literal_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dataset.csv"
            original = fixture()
            original.to_csv(path, index=False)
            loaded = load_asteroids(path)
            self.assertEqual(loaded.loc[0, "id"], "0001")
            self.assertEqual(loaded.loc[0, "spkid"], "00101")
            self.assertEqual(loaded.loc[2, "full_name"], "NA")
            pd.testing.assert_frame_equal(original, loaded, check_exact=True)

    def test_loader_reports_invalid_number_and_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dataset.csv"
            invalid = fixture()
            invalid["diameter"] = invalid["diameter"].astype(object)
            invalid.loc[0, "diameter"] = "not-a-number"
            invalid.to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "diameter.*not-a-number"):
                load_asteroids(path)
            fixture().drop(columns="H").to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "Missing columns.*H"):
                load_asteroids(path)
            fixture().iloc[:0].to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "no object records"):
                load_asteroids(path)

    def test_missing_file_has_actionable_message(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(FileNotFoundError, "Download the Kaggle CSV"):
                load_asteroids(Path(directory) / "missing.csv")

    def test_cleaning_only_trims_names_and_is_idempotent(self):
        original = fixture()
        before = original.copy(deep=True)
        clean, log = prepare_shared_data(original)
        self.assertEqual(clean.loc[0, "full_name"], "Name  A")
        self.assertTrue(pd.isna(clean.loc[1, "full_name"]))
        self.assertEqual(log.loc[0, "Changed cells"], 1)
        self.assertEqual(log.loc[0, "Rows before"], log.loc[0, "Rows after"])
        pd.testing.assert_frame_equal(original, before)
        pd.testing.assert_frame_equal(clean.drop(columns="full_name"), original.drop(columns="full_name"))
        pd.testing.assert_series_equal(clean.isna().sum(), original.isna().sum())
        again, again_log = prepare_shared_data(clean)
        pd.testing.assert_frame_equal(clean, again)
        self.assertEqual(again_log.loc[0, "Changed cells"], 0)

    def test_identifier_problems_block_cleaning(self):
        for col in ["id", "spkid"]:
            for value in [pd.NA, "   ", fixture().loc[1, col]]:
                with self.subTest(column=col, value=value):
                    table = fixture()
                    table.loc[0, col] = value
                    with self.assertRaisesRegex(ValueError, f"{col} has missing/blank or repeated"):
                        prepare_shared_data(table)

    def test_flags_preserve_missing_labels_and_hyperbolic_objects(self):
        table = fixture()
        self.assertFalse(build_review_flags(table).any().any())
        table.loc[0, "per_y"] = 0
        table.loc[1, "moid"] = np.nan
        table.loc[0, "H"] = np.inf
        table.loc[2, "sigma_i"] = -1
        table.loc[2, "i"] = 181
        table.loc[2, "pha"] = "maybe"
        table.loc[2, "class"] = "unknown"
        table.loc[2, "prefix"] = "   "
        flags = build_review_flags(table)
        for row, flag in [
            (0, "flag_nonpositive_period"), (1, "flag_moid_missingness_mismatch"),
            (0, "flag_infinite_H"), (2, "flag_negative_sigma_i"),
            (2, "flag_inclination_out_of_range"), (2, "flag_unexpected_pha"),
            (2, "flag_unexpected_class"), (2, "flag_blank_prefix"),
        ]:
            self.assertTrue(flags.loc[row, flag], flag)
        self.assertFalse(flags.loc[1, "flag_unexpected_pha"])
        self.assertFalse(flags.loc[1, "flag_negative_e"])
        self.assertNotIn("flag_negative_a", flags)
        self.assertTrue(flags.index.equals(table.index))

    def test_export_round_trip_and_raw_preservation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "data/raw/dataset.csv"
            raw.parent.mkdir(parents=True)
            fixture().to_csv(raw, index=False)
            table = load_asteroids(raw)
            clean, log = prepare_shared_data(table)
            flags = build_review_flags(table)
            flags_mask = flags.any(axis=1)
            namespace = dict(FUNCTIONS)
            namespace.update(
                PROJECT_ROOT=root, DATA_PATH=raw, df=table, df_clean=clean,
                raw_sha256=FUNCTIONS["file_sha256"](raw), cleaning_log_df=log,
                review_records=clean.loc[flags_mask].join(flags.loc[flags_mask]),
                review_summary=flags.sum().rename_axis("Check").reset_index(name="Count"),
            )
            exec(CELLS["validate-export"], namespace)
            self.assertEqual(len(list((root / "data/processed").glob("*.csv"))), 4)
            pd.testing.assert_frame_equal(load_asteroids(raw), table, check_exact=True)
            pd.testing.assert_frame_equal(
                load_asteroids(root / "data/processed/asteroids_clean.csv"), clean, check_exact=True
            )


if __name__ == "__main__":
    unittest.main()
