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
- **Original data source / collecting organization:** TODO – verify from the dataset documentation and cite the exact source.
- **License shown on Kaggle:** Database: Open Database License (ODbL) 1.0; Contents: © Original Authors. Read the license and document attribution/share-alike obligations before redistributing any data.
- **Dataset version / download date:** TODO
- **Related public notebooks or prior studies:** TODO – search, list, and explain how this project differs.

## 3. Research questions

The assignment requires **2 × n questions**, where n is the number of team members. At least one question must be answered using a machine-learning model.

| ID | Question | Type (Non-ML / ML) | Owner | D criteria (for Non-ML) | Status |
|---|---|---|---|---|---|
| Q1 | To be decided after data exploration | Non-ML | TODO | TODO | Draft |
| Q2 | To be decided after data exploration | Non-ML | TODO | TODO | Draft |
| Q3 | To be decided after data exploration | Non-ML | TODO | TODO | Draft |
| Q4 | To be decided after data exploration | Non-ML | TODO | TODO | Draft |
| Q5 | To be decided after data exploration | Non-ML | TODO | TODO | Draft |
| Q6 | To be decided after data exploration | ML / Non-ML | TODO | N/A if ML | Draft |

Adjust the number of rows to exactly **2 × n**. The table above is only a starter example for a three-person team, not a final decision.

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
2. Put the CSV file in `data/raw/`.
3. Record the exact filename, download date, source, and version.
4. Update the `DATA_PATH` variable in `01_collection_exploration.ipynb`.

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
