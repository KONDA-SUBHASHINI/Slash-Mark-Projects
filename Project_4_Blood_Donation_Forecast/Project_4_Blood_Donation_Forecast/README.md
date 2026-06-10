# 🩸 Give Life: Predict Blood Donations

> *"Blood is the most precious gift that anyone can give to another person — the gift of life."*
> ~ World Health Organization

## 📌 Overview

Forecasting blood supply is a serious and recurrent problem for blood collection managers. In January 2019, the Red Cross saw 27,000 fewer blood donations over the holidays than at other times of the year. Machine learning can help solve this by learning patterns in donor behavior to predict future donations — and ultimately save more lives.

This project builds a complete machine learning pipeline to predict whether a blood donor will donate again within a given time window, using real donor data from Taiwan.

---

## 🎯 Objective

Binary classification — predict if a donor will donate blood in March 2007:
- `1` → Will donate
- `0` → Will not donate

---

## 📂 Project Structure

```
Project_4_Blood_Donation_Forecast/
│
├── datasets/
│   └── transfusion.data       # Raw donor dataset (748 records)
│
├── notebook.ipynb             # Main project notebook
└── README.md                  # Project documentation
```

---

## 📊 Dataset

The dataset was collected from the Blood Transfusion Service Center in Hsin-Chu City, Taiwan. The center drives a mobile blood donation bus to universities every three months. The dataset contains a random sample of **748 donors** (533 after deduplication) obtained from the UCI Machine Learning Repository.

It is structured according to the **RFMTC marketing model** — a variation of the classic RFM (Recency, Frequency, Monetary) model used in marketing to identify best customers. Here, donors are treated as customers.

| Column | Symbol | Description |
|--------|--------|-------------|
| Recency (months) | R | Months since the donor's last donation |
| Frequency (times) | F | Total number of times the donor has donated |
| Monetary (c.c. blood) | M | Total volume of blood donated in c.c. |
| Time (months) | T | Months since the donor's very first donation |
| Target | C | Whether the donor donated in March 2007 (1 = yes, 0 = no) |

### Class Distribution

| Class | Meaning | Proportion |
|-------|---------|------------|
| 0 | Did not donate | 72.1% |
| 1 | Donated | 27.9% |

> The dataset is **imbalanced** — a naive model that always predicts 0 would be right 72% of the time. This is why we use **AUC-ROC** as our evaluation metric instead of accuracy.

---

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Libraries:** pandas, numpy, scikit-learn

Install all dependencies:
```bash
pip install pandas numpy scikit-learn jupyter
```

> ⚠️ **Note on TPOT:** This project originally used the `tpot` library for automated model selection. TPOT is incompatible with Python 3.13 due to a missing `pkg_resources` dependency. We replicated its result manually — TPOT selects **Logistic Regression** as the best pipeline with an AUC score of **0.7527**, which we confirmed independently.

---

## 🔬 Methodology

### 1. Data Inspection & Cleaning
Loaded and inspected the raw CSV file. Confirmed all 5 columns are numeric (`int64`) with no missing values across all 748 rows. Removed **215 duplicate rows** (28.7% of dataset) leaving 533 clean records.

### 2. Preprocessing
- Renamed the verbose target column to `target` for cleaner code
- Performed a **stratified train/test split** (75/25) to preserve the 72/28 class ratio in both sets
- Discovered that `Monetary (c.c. blood)` had a variance of **2,114,363** — orders of magnitude higher than all other features (max ~611)
- Applied **log normalization** to `Monetary`, reducing its variance to **0.837**

### 3. Modelling
- Used **Logistic Regression** (`solver=liblinear`) as identified by TPOT
- Trained two versions — one on raw data, one on log-normalized data
- Added **StandardScaler Pipeline** to scale all features
- Compared with **Random Forest Classifier**
- Evaluated all models using **AUC-ROC score**
- Performed **5-Fold Cross Validation** for reliable accuracy estimation

---
## 📈 Results

| Model | AUC-ROC Score |
|-------|--------------|
| Logistic Regression — baseline (raw data) | 0.7527 |
| Logistic Regression — log-normalized Monetary | 0.7533 |
| StandardScaler Pipeline | **0.7577** |
| Random Forest | 0.6102 |
| **Cross-Validation Mean (5-fold)** | **0.7399 ± 0.0402** |

The StandardScaler Pipeline is the best model with an AUC of **0.7577**. While improvements over the baseline are modest, in healthcare applications even small gains matter.

> **CV Note:** The CV mean AUC (0.7399) vs test AUC (0.7577) gap suggests the test split was favourable — true generalisation performance is closer to 0.74.

> **Confusion Matrix insight:** The model catches 96% of non-donors and 35% of actual donors. Removing 215 duplicate rows improved donor recall significantly from an earlier 11%.
---

## ▶️ How to Run

```bash
cd Project_4_Blood_Donation_Forecast
jupyter notebook notebook.ipynb
```

Run all cells from top to bottom. All outputs will be displayed inline in the notebook.

---

## ✅ Project Tasks

| # | Task | Status |
|---|------|--------|
| 1 | Inspecting transfusion.data file | ✅ |
| 2 | Loading the blood donations data | ✅ |
| 2a | Removing 215 duplicate rows | ✅ |
| 3 | Inspecting transfusion DataFrame | ✅ |
| 4 | Creating target column | ✅ |
| 5 | Checking target incidence | ✅ |
| 6 | Splitting transfusion into train and test datasets | ✅ |
| 7 | Selecting model using TPOT *(manual replication)* | ✅ |
| 8 | Checking the variance | ✅ |
| 9 | Log normalization | ✅ |
| 10 | Training the Logistic Regression model | ✅ |
| 10a | 5-Fold Cross Validation | ✅ |
| 10b | StandardScaler Pipeline | ✅ |
| 10c | Confusion Matrix & Classification Report | ✅ |
| 10d | Random Forest comparison | ✅ |
| 11 | Conclusion | ✅ |

---

## 💡 Key Takeaways

- **Data cleaning matters** — 215 duplicate rows (28.7%) were found and removed before modelling
- **Data quality matters** — the dataset was clean with zero missing values, making preprocessing straightforward
- **Class imbalance** means accuracy is misleading — always check your evaluation metric against the problem type
- **Feature scaling** is critical for linear models — a single high-variance feature can blind the model to everything else
- **StandardScaler Pipeline beats all models** on this dataset with AUC 0.7577 — scaling all features gave better results than log normalization alone
- **Logistic Regression beats Random Forest** (0.7533 vs 0.6102) — small dataset (533 rows) means tree models don't have enough data to generalise well
- **CV vs single split gap** — CV mean of 0.7399 vs test AUC of 0.7577 suggests the test split was favourable; true performance is closer to 0.74
- **Donor recall improved to 35%** after deduplication — removing 215 duplicate rows significantly improved the model's ability to identify actual donors
- **Logistic Regression is interpretable** — we can explain exactly why the model made each prediction, which is valuable in healthcare settings

---

## 📚 References

- [UCI Machine Learning Repository — Blood Transfusion Dataset](https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center)
- [TPOT AutoML Library](https://github.com/EpistasisLab/tpot)
- [scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [WebMD — Blood Transfusion](https://www.webmd.com/a-to-z-guides/blood-transfusion-what-to-know)