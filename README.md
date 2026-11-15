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

The group has not selected research questions yet. Relationships between
variables, hypothesis tests, feature engineering and machine learning are for a
later phase. The question-count/D1–D6/ML requirements in the initial scaffold
must be checked separately against the applicable assignment; they are not
acceptance criteria for this preprocessing phase.

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

Notebook 01 is the deliverable for the current phase. Notebooks 02 and 03 remain
templates for work after research questions are selected.

## 6. Key findings

To be completed after the analysis. Report 3–5 evidence-based findings.

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
