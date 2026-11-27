# Asteroid Data Science Project

> Course: CSC17104 – Programming for Data Science  
> Dataset: Asteroid Dataset (Kaggle)  
> Dataset approval: Reported as approved by the instructor; retain the approval record if available.

## 1. Team

| Member | Student ID | GitHub username | Main responsibilities |
|---|---|---|---|
| Nam | — | — | Q1, Q2 |
| Nghiêm | — | — | Q3, Q5 |
| Kiệt | — | — | Q4, Q6 |

Nhóm sẽ bổ sung họ tên đầy đủ và MSSV.

## 2. Project overview

- **Topic:** Asteroids and their physical/orbital characteristics.
- **Main objective:** Use real-world asteroid data to investigate meaningful questions through data exploration, statistical analysis, visualization, and at least one machine-learning question.
- **Dataset page:** https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset
- **Original data source / collecting organization:** [NASA/JPL Small-Body Database](https://ssd-api.jpl.nasa.gov/doc/sbdb.html).
- **License shown on Kaggle:** Database: Open Database License (ODbL) 1.0; Contents: © Original Authors. Read the license and document attribution/share-alike obligations before redistributing any data.
- **Dataset version / download date:** TODO
- **Related public notebooks or prior studies:** TODO – search, list, and explain how this project differs.

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

1. Download the dataset from the Kaggle page.
2. Đặt CSV đã giải nén tại `data/raw/dataset.csv`.
3. Record the exact filename, download date, source, and version.
4. Notebook 01 đọc đường dẫn trên và xuất các bảng vào `data/processed/`.

Q6 trong Notebook 03 dùng thêm [bản chu kỳ tự quay NASA/JPL](data/external/README.md) đã lưu trong repo.

### Run notebooks in order

1. `01_collection_exploration.ipynb`
2. `02_analysis.ipynb`
3. `03_ml_question.ipynb`

## 6. Key findings

To be completed after the analysis. Report 3–5 evidence-based findings.

## 7. Limitations and future work

To be completed after the analysis.

## 8. Work plan

See `docs/PROJECT_PLAN.md`. Add the shared task-board link here when the team creates one.

## 9. References

- Kaggle dataset: https://www.kaggle.com/datasets/sakhawat18/asteroid-dataset
- Original source documentation: TODO
- Related research / public notebooks: TODO
