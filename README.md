# Asteroid Data Science Project

> Course: CSC17104 – Programming for Data Science  
> Dataset: Asteroid Dataset (Kaggle)  
> Dataset approval: Reported as approved by the instructor; retain the approval record if available.

## 1. Team

| Thành viên | MSSV | Phụ trách |
|---|---|---|
| Nguyễn Thành Nam | 24120386 | Q1, Q2 |
| Hồ Hữu Nghiêm | 24120390 | Q3, Q5 |
| Phùng Đức Tuấn Kiệt | 24120358 | Q4, Q6 |

## 2. Project overview

- **Topic:** Asteroids and their physical/orbital characteristics.
- **Main objective:** Use real-world asteroid data to investigate meaningful questions through data exploration, statistical analysis, visualization, and at least one machine-learning question.
- **Dataset page:** [Asteroid Dataset](https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset), do Mir Sakhawat Hossain đăng trên Kaggle.
- **Original data source / collecting organization:** [NASA/JPL Small-Body Database](https://ssd-api.jpl.nasa.gov/doc/sbdb.html).
- **Giấy phép hiển thị trên Kaggle:** `Database: Open Database, Contents: © Original Authors`. Xem ghi chú giấy phép trên trang dữ liệu trước khi phân phối lại.
- **Phiên bản kiểm tra:** Kaggle v328, phát hành ngày 25/11/2026 và tải kiểm tra ngày 28/11/2026. File `dataset.csv` có 958.524 dòng và 45 cột. Đối chiếu mã SHA-256 dưới đây để xác nhận file dùng trong lần chạy cuối.
- **Phân tích công khai:** [Các notebook gắn với bộ dữ liệu trên Kaggle](https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset/code). Các tài liệu nhóm sử dụng được ghi trong mục tài liệu tham khảo của từng notebook.

```text
SHA-256  022037701b45bf61f090078715d1318324189683400c10bc4aae8b71081b835e  dataset.csv
```

## 3. Research questions

The assignment requires **2 × n questions**, where n is the number of team members. At least one question must be answered using a machine-learning model.

| Câu | Câu hỏi | Loại | Phụ trách | Tiêu chí | Notebook |
|---|---|---|---|---|---|
| Q1 | Hình dạng quỹ đạo liên hệ thế nào với MOID và tỷ lệ PHA khi xét theo lớp và độ nghiêng quỹ đạo? | Non-ML | Nam | D3, D4, D5, D6 | 02 |
| Q2 | Đường kính và suất phản chiếu thay đổi thế nào theo vùng quỹ đạo khi so các vật thể cùng khoảng độ sáng H? | Non-ML | Nam | D3, D4, D5, D6 | 02 |
| Q3 | Nhóm quỹ đạo nào có dữ liệu vật lý đầy đủ nhất trước và sau chuẩn hóa theo H? | Non-ML | Nghiêm | D2, D3, D4, D6 | 02 |
| Q4 | Ở cùng khoảng đường kính, nhóm C hay S có tỷ lệ bề mặt tối cao hơn? | Non-ML | Kiệt | D1, D2, D3, D4 | 02 |
| Q5 | Biết thêm quỹ đạo có giúp ước lượng đường kính chính xác hơn so với chỉ biết H? | ML | Nghiêm | — | 03 |
| Q6 | Độ sáng và quỹ đạo có giúp ước lượng chu kỳ tự quay và tìm các vật thể quay một vòng trong tối đa 8 giờ? | ML | Kiệt | — | 03 |

### Non-ML depth checklist

Each Non-ML question must clearly use at least two criteria, and the questions together must cover at least four of these six criteria:

- D1 – Combining data
- D2 – Reshaping & time
- D3 – Derived variables
- D4 – Controlling for a confounder
- D5 – Quantifying uncertainty
- D6 – Robustness check

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
│   ├── external/
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

1. Tải [bản v328 trên Kaggle](https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset/versions/328).
2. Giải nén `dataset.csv` vào `data/raw/`. Có thể kiểm tra file bằng `sha256sum data/raw/dataset.csv` trên Linux hoặc WSL.
3. Notebook 01 xuất các bảng vào `data/processed/`. Notebook 02 và 03 đọc CSV gốc, sau đó xử lý dữ liệu theo từng câu hỏi.

Q6 trong Notebook 03 dùng thêm [bản chu kỳ tự quay NASA/JPL](data/external/README.md) đã lưu trong repo.

### Run notebooks in order

Mở từng notebook bằng kernel `asteroid-pds` và chọn **Restart Kernel and Run All Cells**.

1. [Thu thập, khám phá và tiền xử lý](notebooks/01_collection_exploration.ipynb)
2. [Phân tích Q1–Q4](notebooks/02_analysis.ipynb)
3. [Học máy Q5–Q6](notebooks/03_ml_question.ipynb)

Khi chốt kết quả, chạy `conda list` để ghi phiên bản `python`, `pandas` và `scikit-learn` đã dùng. Đối chiếu số làm tròn giữa đầu ra notebook, README và slide của cùng lần chạy.

## 6. Key findings

Nhóm bổ sung 3–5 phát hiện từ kết quả chạy chốt trong [Notebook 02](notebooks/02_analysis.ipynb) và [Notebook 03](notebooks/03_ml_question.ipynb), kèm số liệu và câu hỏi tương ứng.

## 7. Limitations and future work

Nhóm bổ sung hạn chế về dữ liệu, phương pháp và phạm vi áp dụng, cùng hướng phát triển tiếp theo.

## 8. Phản tư cá nhân

Nam, Nghiêm và Kiệt mỗi người tự ghi phần mình phụ trách, khó khăn và cách xử lý, điều đã học và cách đã sử dụng LLM.

## 9. References

- Kaggle dataset: https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset
- [NASA/JPL Small-Body Database API](https://ssd-api.jpl.nasa.gov/doc/sbdb.html) và [định nghĩa các trường dữ liệu](https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html).
- [NASA/JPL CNEOS – Phân loại NEO và PHA](https://cneos.jpl.nasa.gov/about/neo_groups.html) và [quan hệ giữa H, albedo và đường kính](https://cneos.jpl.nasa.gov/tools/ast_size_est.html).
- [Bản chụp dữ liệu bổ sung cho Q4 và Q6](data/external/README.md).
- [Stroke-Prediction-Analysis](https://github.com/Ddyln/Stroke-Prediction-Analysis), tài liệu tham khảo bố cục đánh giá mô hình được ghi ở Q5.
