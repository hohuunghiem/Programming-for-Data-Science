# Asteroid Data Science Project

> Course: CSC17104 – Programming for Data Science  
> Dataset: Asteroid Dataset (Kaggle)  
> Dataset approval: Reported as approved by the instructor; retain the approval record if available.

## 1. Team

| Member | Student ID | GitHub username | Main responsibilities |
|---|---|---|---|
| Member 1 | TODO | TODO | TODO |
| Member 2 | TODO | TODO | TODO |
| Member 3 (if applicable) | TODO | TODO | TODO |

Update the table to match the actual team size.

## 2. Project overview

- **Topic:** Asteroids and their physical/orbital characteristics.
- **Main objective:** Use real-world asteroid data to investigate meaningful questions through data exploration, statistical analysis, visualization, and at least one machine-learning question.
- **Dataset page:** https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset
- **Original data documentation:** NASA/JPL Small-Body Database (SBDB); [field definitions](https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html) and [orbital classifications](https://ssd-api.jpl.nasa.gov/doc/sbdb_filter.html). The CSV is a catalogue snapshot, not raw telescope observations.
- **License:** The initial scaffold recorded `Database: Open Database License (ODbL) 1.0; Contents: © Original Authors`. Confirm this on the downloaded Kaggle version before redistribution; the ZIP contains no license file.
- **Local download:** Supplied by the team on 2026-11-16 as `archive.zip`; extracted `dataset.csv` is 456,576,403 bytes. The ZIP does not identify its Kaggle version number, which still needs confirmation. Notebook 01 prints the source SHA-256 for reproducibility.
- **Related public notebooks or prior studies:** TODO – search, list, and explain how this project differs.

### Current phase: basic preprocessing

Notebook 01 documents every column, checks identifiers/duplicates/missingness,
summarizes individual variables, trims outer whitespace in `full_name`, and
exports a minimally cleaned dataset with separate quality-review files. Records,
columns, missing measurements and rare classes are retained. Suspicious values
are flagged for review rather than automatically removed or filled.

Notebook 01 remains the basic-preprocessing deliverable. At the requesting
member's direction, Notebook 02 now develops four proposed Non-ML questions
(Q1–Q4) covering D1–D4, with Vietnamese explanations, executed results and figures. These are proposals awaiting team approval; Q5–Q6 and ML are still open.
The question-count/D1–D6/ML requirements in the initial scaffold must be checked
separately against the applicable assignment.

## 3. Research questions

The assignment requires **2 × n questions**, where n is the number of team members. At least one question must be answered using a machine-learning model.

| ID | Question | Type (Non-ML / ML) | Owner | D criteria (for Non-ML) | Status |
|---|---|---|---|---|---|
| Q1 | Sau khi ghép phân loại phổ SMASSII từ JPL vào dataset, nhóm phổ C và S có tỷ lệ albedo dưới 0,10 chênh lệch bao nhiêu điểm phần trăm khi so sánh cùng khoảng đường kính? | Non-ML | TODO — phần Q1–Q4 | D1, D3, D4 | Đã chạy; chờ nhóm duyệt |
| Q2 | Trong từng khoảng độ sáng tuyệt đối H, nhóm NEO và không-NEO có tỷ lệ được ghi nhận đường kính, albedo và độ bất định đường kính khác nhau thế nào? Nhóm nào có tỷ lệ đủ cả H–đường kính–albedo cao hơn? | Non-ML | TODO — phần Q1–Q4 | D2, D3, D4 | Đã chạy; chờ nhóm duyệt |
| Q3 | Với các đối tượng có đủ H, albedo và đường kính, nếu tính đường kính từ H với albedo cố định 0,15, kết quả thường cao hay thấp hơn đường kính ghi nhận bao nhiêu phần trăm, và khác nhau thế nào giữa các nhóm albedo? | Non-ML | TODO — phần Q1–Q4 | D3, D4 | Đã chạy; chờ nhóm duyệt |
| Q4 | So với MBA, OMB và TJN có tỷ lệ đối tượng có albedo dưới 0,10 chênh lệch bao nhiêu điểm phần trăm khi so sánh cùng khoảng đường kính? | Non-ML | TODO — phần Q1–Q4 | D3, D4 | Đã chạy; chờ nhóm duyệt |
| Q5 | To be decided after data exploration | Non-ML | TODO | TODO | Draft |
| Q6 | To be decided after data exploration | ML / Non-ML | TODO | N/A if ML | Draft |

Adjust the number of rows to exactly **2 × n**. The table above is only a starter example for a three-person team, not a final decision.

### Non-ML depth checklist

Bộ Q1–Q4 hiện tại tập trung vào **D1–D4**: mỗi câu dùng ít nhất hai tiêu chí,
cả bộ bao phủ đủ bốn tiêu chí. Không gán D5/D6 cho bộ câu hỏi này.

- D1 — Combining data: Q1 ghép nhãn phổ SMASSII của JPL vào Kaggle theo `pdes`.
- D2 — Reshaping & time: Q2 dùng `melt`/`pivot` cho độ bao phủ nhiều loại thông tin;
  chỉ dùng reshaping, không coi `epoch` là ngày phát hiện.
- D3 — Derived variables: cờ albedo thấp, có số đo, đủ bộ thông tin, khoảng H/đường kính và mức lệch kích thước.
- D4 — Controlling for a confounder: xét các nhóm trong cùng khoảng H/đường kính
  và dùng cùng cơ cấu tầng để so sánh.

### ML question checklist

- Define a prediction task, intended user, target, and prediction-time features.
- Identify and exclude leakage columns.
- Choose an appropriate train/test split (time-based or group-based where appropriate).
- Compare at least two ML models and one trivial baseline.
- Put preprocessing inside a scikit-learn Pipeline.
- Tune with cross-validation on the training set only.
- Evaluate on the test set once using justified metrics.
- Analyse errors and interpret the model.

## 4. Repository structure

```text
project-name/
├── README.md
├── environment.yml
├── LLM_USAGE.md
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── notebooks/
│   ├── 01_collection_exploration.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_ml_question.ipynb
├── docs/
│   ├── TONIGHT_MEETING.md
│   ├── QUESTION_BANK_TEMPLATE.md
│   └── PROJECT_PLAN.md
└── slides.pdf
```

Large raw data files should not be committed to GitHub. Follow the dataset license and provide download instructions instead.

## 5. How to run

### Create the Conda environment

```bash
conda env create -f environment.yml
conda activate asteroid-pds
python -m ipykernel install --user --name asteroid-pds --display-name "Python (asteroid-pds)"
jupyter lab
```

### Add the dataset

1. Download the dataset from the [Kaggle page](https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset).
2. Extract `dataset.csv` to `data/raw/dataset.csv`; do not modify this raw file.
3. Record the downloaded version, date and license. The local file is ignored by Git.
4. Open `01_collection_exploration.ipynb` from the repository root or `notebooks/`, select the environment's kernel, and use **Restart Kernel and Run All**.

### Basic preprocessing outputs

Notebook 01 writes these files to `data/processed/` after identifier and value-preservation checks:

| File | Contents |
|---|---|
| `asteroids_clean.csv` | All source records/columns, with trimmed object names |
| `cleaning_log.csv` | Applied changes and before/after row counts |
| `records_to_review.csv` | Flagged records and Boolean flags naming affected fields/issues |
| `quality_review_summary.csv` | Counts for all quality checks; flags may overlap |

Rerunning replaces generated files. The notebook verifies the raw checksum and
reloads the main export to check values and identifiers. A parse error or a
missing/blank/repeated `id` or `spkid` stops the run for review. A flagged value
remains in the export; the review file does not establish that it is an error.

CSV does not preserve pandas dtypes. To reload the shared file:

```python
from pathlib import Path
import pandas as pd

project_root = Path.cwd()
if project_root.name == "notebooks":
    project_root = project_root.parent
text_columns = [
    "id", "spkid", "full_name", "pdes", "name", "prefix",
    "neo", "pha", "orbit_id", "equinox", "class",
]
df = pd.read_csv(
    project_root / "data/processed/asteroids_clean.csv",
    dtype={col: "string" for col in text_columns},
    keep_default_na=False, na_values=[""],
    low_memory=False, float_precision="round_trip",
)
```

Run the small preprocessing checks from the repository root:

```bash
python -m unittest discover -s tests -v
```

### Chạy phân tích Q1–Q4 theo D1–D4

Sau Notebook 01, chạy `02_analysis.ipynb` bằng **Restart Kernel and Run All**.
Mỗi câu có lý do, định nghĩa chính xác, quy trình, giải thích code, hai biểu đồ,
kết quả bằng số và giới hạn. D5/D6 không phải trọng tâm của phiên bản này.

Q1 cần thêm bản phân loại phổ SMASSII từ **JPL SBDB Query API**. Lần đầu,
notebook tải các trường `spkid,pdes,spec_B` cho đối tượng có `spec_B`; các lần
sau đọc lại `data/raw/jpl_smassii_taxonomy.json` và metadata đi kèm. Không cần
thư viện hoặc tài khoản bổ sung. URL, thời điểm tải và SHA-256 được lưu để đối chiếu.
Hai file này được Git bỏ qua; muốn tái lập đúng bản chụp, nhóm cần dùng cùng
hai file và đối chiếu SHA-256 đã lưu trong output notebook. Nếu tải lại ở thời
điểm khác, nhãn/độ bao phủ có thể thay đổi.

- Q1 ghép **1–1 theo `pdes`** bằng left join, báo khóa không khớp và giữ các
  cột Kaggle nguyên vẹn. `spkid` không khớp trực tiếp giữa hai bản nguồn;
  không đổi ID theo công thức phỏng đoán.
- Nhãn JPL là thông tin lúc tải, không được coi là nhãn lịch sử tại thời điểm
  bản Kaggle được xuất. Chỉ bổ sung loại phổ, không cập nhật các số đo cũ.
- Q2 báo số dòng trước/sau `melt` và kiểm tra pivot khôi phục đúng tỷ lệ.
- Phép chuẩn hóa báo cả toàn tập, vùng chung và cơ cấu trọng số. Kết quả mô tả
  các bản ghi có thông tin, không chứng minh nhân quả hay tính đại diện toàn quần thể.

Các bảng mới nằm trong `data/processed/d1_d4/` (Git bỏ qua). Bảng cũ trong
`data/processed/q1_q4/` không phải đầu ra của phiên bản D1–D4. Các hàm dùng
chung nằm trong `src/nonml_analysis.py`; Notebook 03 vẫn là template.

## 6. Key findings

Kết quả phiên bản **D1–D4**, trên CSV nhóm tải ngày 16/11/2026 và bản chụp
phân loại phổ JPL được ghi trong metadata (xem mẫu số/giới hạn trong Notebook 02):

- **Q1 (D1/D3/D4):** Bảng JPL có 1.666 đối tượng; ghép được 1.659 theo `pdes`,
  7 đối tượng JPL không khớp. Trong vùng đường kính chung, tỷ lệ albedo <0,10
  chuẩn hóa là C 87,92%, S 1,29%; chênh lệch C−S +86,62 điểm phần trăm.
- **Q2 (D2/D3/D4):** `melt` chuyển 18 dòng thống kê nhóm thành 72 dòng
  nhóm–loại thông tin; `pivot` bảo toàn các tỷ lệ. Sau chuẩn hóa H, tỷ lệ đủ
  H–diameter–albedo là không-NEO 11,83%, NEO 24,62% trong vùng chung.
- **Q3 (D3/D4):** Trên 131.237 bản ghi có đủ H–diameter–albedo, giả định
  albedo 0,15 cho trung vị lệch −32,53% và MdAPE 36,49% so với diameter ghi
  nhận. Đây không phải phép xác thực độc lập vì các trường có thể được suy ra cùng nhau.
- **Q4 (D3/D4):** Sau chuẩn hóa khoảng đường kính, chênh lệch tỷ lệ albedo
  <0,10 là OMB−MBA +27,22 và TJN−MBA +14,13 điểm phần trăm, trong vùng chung riêng của từng cặp.

## 7. Limitations and future work

To be completed after the analysis.

## 8. Work plan

See `docs/PROJECT_PLAN.md`. Add the shared task-board link here when the team creates one.

## 9. References

- Kaggle dataset: https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset
- JPL field documentation: https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html
- JPL orbital classifications: https://ssd-api.jpl.nasa.gov/doc/sbdb_filter.html
- Basic-exploration presentation examples: [P4DS-final](https://github.com/BoonRealCuaaaaa/P4DS-final/blob/main/02_Exploring-and-Preprocessing.ipynb), [Stroke Prediction Analysis, section III](https://github.com/Ddyln/Stroke-Prediction-Analysis/blob/main/report.ipynb). Used for structure, not copied cleaning rules.
- Related research / public notebooks: TODO

- Nguồn bổ sung cho Q1: [JPL SBDB Query API](https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html), trường `spec_B` (SMASSII).
