import ast
import json
from pathlib import Path
import tempfile
import unittest

import pandas as pd

from src.nonml_analysis import load_taxonomy, merge_taxonomy, standardized_rates


class NonMLAnalysisTests(unittest.TestCase):
    def test_q1_answer_uses_join_result_not_display_column(self):
        # Bảng log có thể đổi nhãn hiển thị; số khớp phải lấy từ kết quả merge.
        path = Path(__file__).resolve().parents[1] / "notebooks/02_analysis.ipynb"
        notebook = json.loads(path.read_text(encoding="utf-8"))
        answer = next(
            node
            for cell in notebook["cells"] if cell["cell_type"] == "code"
            for node in ast.walk(ast.parse("".join(cell["source"])))
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == "Markdown" and "Trả lời Q1" in ast.unparse(node)
        )
        text = eval(compile(ast.Expression(answer.args[0]), str(path), "eval"), {
            "joined": pd.DataFrame({"_merge": ["both", "left_only", "both"]}),
            "q1": pd.DataFrame(index=range(2)),
            "q1_adjusted": {"target_rate": .8, "reference_rate": .2, "difference": .6},
        })
        self.assertIn("Ghép được **2**", text)

    def test_load_snapshot_validates_fields_and_count(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "taxonomy.json"
            payload = {"fields": ["spkid", "pdes", "spec_B"], "count": "2",
                       "data": [[20000001, "1", "C"], [20000003, "3", "Sk"]]}
            path.write_text(json.dumps(payload), encoding="utf-8")
            table = load_taxonomy(path)
            self.assertEqual(table.loc[0, "pdes"], "1")
            self.assertEqual(table.loc[0, "jpl_spkid"], "20000001")
            payload["count"] = "3"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Số bản ghi"):
                load_taxonomy(path)

    def test_join_uses_designation_despite_changed_spkid(self):
        base = pd.DataFrame({"id": ["a1", "a2"], "pdes": ["1", "2"],
                             "spkid": ["2000001", "2000002"], "albedo": [.1, .2]}).astype({"pdes": "string"})
        taxonomy = pd.DataFrame({"pdes": ["1", "3"], "jpl_spkid": ["20000001", "20000003"],
                                 "spec_B": ["C", "Sk"]}).astype("string")
        joined, audit, unmatched = merge_taxonomy(base, taxonomy)
        self.assertEqual(len(joined), len(base))
        self.assertEqual(joined.loc[0, "spec_B"], "C")
        self.assertTrue(pd.isna(joined.loc[1, "spec_B"]))
        pd.testing.assert_frame_equal(joined[base.columns], base)
        self.assertEqual(unmatched.pdes.tolist(), ["3"])
        self.assertEqual(audit.loc[0, "Khớp phân loại JPL"], 1)

    def test_duplicate_or_missing_join_keys_are_rejected(self):
        base = pd.DataFrame({"pdes": ["1", "2"]})
        for keys in [["1", " 1 "], ["1", None], ["1", " "]]:
            taxonomy = pd.DataFrame({"pdes": keys, "jpl_spkid": ["x", "y"], "spec_B": ["C", "S"]})
            with self.subTest(keys=keys), self.assertRaisesRegex(ValueError, "Khóa pdes"):
                merge_taxonomy(base, taxonomy)

    def test_standardization_removes_composition_difference(self):
        frame = pd.DataFrame({
            "group": ["A"] * 100 + ["B"] * 100,
            "stratum": ["low"] * 80 + ["high"] * 20 + ["low"] * 20 + ["high"] * 80,
            "outcome": [0] * 80 + [1] * 20 + [0] * 20 + [1] * 80,
        })
        r, detail = standardized_rates(frame, "group", "outcome", ["stratum"], "A", "B", 10)
        self.assertAlmostEqual(r["difference"], 0)
        self.assertAlmostEqual(r["reference_rate"], .5)
        self.assertAlmostEqual(r["reference_common_rate"], .2)
        self.assertAlmostEqual(r["target_common_rate"], .8)
        self.assertAlmostEqual(detail.weight.sum(), 1)

    def test_sparse_strata_and_invalid_outcomes(self):
        frame = pd.DataFrame({"group": ["A", "A", "B", "B", "A"],
                              "stratum": ["common"] * 4 + ["alone"], "outcome": [1, 0, 1, 1, 1]})
        r, _ = standardized_rates(frame, "group", "outcome", ["stratum"], "A", "B", 2)
        self.assertEqual(r["n_reference"], 2)
        self.assertEqual(r["n_strata"], 1)
        with self.assertRaisesRegex(ValueError, "Không có tầng"):
            standardized_rates(frame, "group", "outcome", ["stratum"], "A", "B", 3)
        frame.loc[0, "outcome"] = 2
        with self.assertRaisesRegex(ValueError, "0/1"):
            standardized_rates(frame, "group", "outcome", ["stratum"], "A", "B", 2)


if __name__ == "__main__":
    unittest.main()
