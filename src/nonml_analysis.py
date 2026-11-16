"""Đọc/ghép bảng phân loại phổ và chuẩn hóa tỷ lệ cho Notebook 02 (D1–D4)."""

import json

import numpy as np
import pandas as pd


def load_taxonomy(path):
    """Đọc bản chụp JSON của JPL; không gọi mạng hoặc tự sửa nhãn phân loại."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("fields") != ["spkid", "pdes", "spec_B"]:
        raise ValueError("Bảng JPL phải có đúng các trường spkid, pdes, spec_B theo thứ tự.")
    records = payload.get("data", [])
    if not records or len(records) != int(payload.get("count", -1)):
        raise ValueError("Số bản ghi JPL không khớp count hoặc bảng rỗng.")
    table = pd.DataFrame(records, columns=payload["fields"]).astype("string")
    if table.isna().any().any():
        raise ValueError("Bảng phân loại đã chọn phải có đầy đủ ba trường.")
    return table.rename(columns={"spkid": "jpl_spkid"})


def merge_taxonomy(asteroids, taxonomy):
    """Left join theo pdes, kiểm tra 1–1 và giữ toàn bộ bản ghi Kaggle."""
    left, right = asteroids.copy(), taxonomy.copy()
    for table in [left, right]:
        table["designation_key"] = table.pdes.astype("string").str.strip()
        key = table.designation_key
        if key.isna().any() or key.eq("").any() or key.duplicated().any():
            raise ValueError("Khóa pdes sau trim bị thiếu/rỗng/trùng; cần kiểm tra trước khi ghép.")
    combined = left.merge(
        right[["designation_key", "jpl_spkid", "spec_B"]], on="designation_key",
        how="left", validate="one_to_one", indicator=True, sort=False,
    )
    assert len(combined) == len(asteroids)
    pd.testing.assert_frame_equal(
        combined[asteroids.columns].reset_index(drop=True), asteroids.reset_index(drop=True)
    )
    unmatched = right.loc[~right.designation_key.isin(left.designation_key)].copy()
    audit = pd.DataFrame([{
        "Số dòng Kaggle trước ghép": len(left), "Số dòng JPL": len(right),
        "Số dòng sau left join": len(combined),
        "Khớp phân loại JPL": int(combined._merge.eq("both").sum()),
        "Kaggle không có nhãn JPL": int(combined._merge.eq("left_only").sum()),
        "JPL không có đối tượng tương ứng trong Kaggle": len(unmatched),
    }])
    return combined, audit, unmatched


def standardized_rates(table, group, outcome, strata, reference, target, min_n=30):
    """Cho hai nhóm cùng cơ cấu tầng; outcome 0/1, không tính khoảng tin cậy."""
    if not strata or min_n < 1:
        raise ValueError("Cần biến phân tầng và ngưỡng số mẫu dương.")
    work = table.loc[table[group].isin([reference, target]), [group, outcome, *strata]]
    if work.isna().any().any() or not work[outcome].isin([0, 1]).all():
        raise ValueError("Cần dữ liệu phân tầng đầy đủ và biến kết quả 0/1.")
    grouped = work.groupby([*strata, group], observed=True)[outcome].agg(n="size", rate="mean").unstack(group)
    if reference not in grouped["n"] or target not in grouped["n"]:
        raise ValueError("Thiếu một nhóm so sánh.")
    common = (grouped["n"][reference] >= min_n) & (grouped["n"][target] >= min_n)
    grouped = grouped.loc[common]
    if grouped.empty:
        raise ValueError("Không có tầng chung đủ số mẫu.")
    detail = pd.DataFrame(index=grouped.index)
    for name, value in [("reference", reference), ("target", target)]:
        detail[f"n_{name}"] = grouped["n"][value].astype(int)
        detail[f"rate_{name}"] = grouped["rate"][value]
    detail["weight"] = (detail.n_reference + detail.n_target)
    detail["weight"] /= detail["weight"].sum()
    result = {
        "reference_common_rate": float((detail.n_reference * detail.rate_reference).sum() / detail.n_reference.sum()),
        "target_common_rate": float((detail.n_target * detail.rate_target).sum() / detail.n_target.sum()),
        "reference_rate": float((detail.weight * detail.rate_reference).sum()),
        "target_rate": float((detail.weight * detail.rate_target).sum()),
        "difference": float((detail.weight * (detail.rate_target - detail.rate_reference)).sum()),
        "n_reference": int(detail.n_reference.sum()), "n_target": int(detail.n_target.sum()),
        "n_strata": len(detail),
    }
    assert np.isclose(detail.weight.sum(), 1)
    return result, detail
