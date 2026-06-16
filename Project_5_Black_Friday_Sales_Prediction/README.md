# 🛍️ Black Friday Sales Prediction

![Black Friday](https://searchengineland.com/figz/wp-content/seloads/2014/12/black-friday1-ss-1920.jpg)

## Table of Contents
- [Project Introduction](#project-introduction)
- [Project Structure](#project-structure)
- [Dataset Description](#dataset-description)
- [EDA](#eda)
- [Data Preprocessing](#data-preprocessing)
- [Modeling Phase](#modeling-phase)
- [Evaluation Metric](#evaluation-metric)
- [Results](#results)
- [Conclusion](#conclusion)
- [How to Run](#how-to-run)
- [Technologies Used](#technologies-used)

---

## Project Introduction

Black Friday is an informal name for the Friday following Thanksgiving Day in the United States, celebrated on the fourth Thursday of November. It has been regarded as the beginning of the Christmas shopping season since 1952 and is one of the biggest retail sales events of the year.

The major challenge for a retail store or eCommerce business is to predict customer purchase amounts so they can personalize offers and maximize profit. This project builds a machine learning pipeline to predict the **purchase amount** of customers against various products, using historical retail store transaction data. After generating predictions, the model helps retail stores decide product pricing to earn more profits.

---

## Project Structure

```
Project_5_Black_Friday_Sales_Prediction/
│
├── Data/
│   └── BlackFridaySales.csv             # Raw dataset
│
├── models/
│   └── xgb_best_model.pkl               # Saved XGBoost model
│
├── Black Friday Sales Prediction.ipynb  # Main notebook
└── README.md
```

---

## Dataset Description

The dataset is sourced from an online data analytics hackathon hosted by **Analytics Vidhya**. It contains purchase transaction records from a retail store during Black Friday.

| Column | Description |
|--------|-------------|
| User_ID | Unique User ID |
| Product_ID | Unique Product ID |
| Gender | Sex of User (M/F) |
| Age | Age in bins |
| Occupation | Occupation (masked) |
| City_Category | Category of City (A, B, C) |
| Stay_In_Current_City_Years | No. of years in current city |
| Marital_Status | Marital Status (0 = Unmarried, 1 = Married) |
| Product_Category_1/2/3 | Product category (masked) |
| **Purchase** | **Target — Purchase Amount ($)** |

- Total records  : 550,068
- Total columns  : 12
- Missing values : Product_Category_2 (~31%) and Product_Category_3 (~69%)

---

## EDA

Key observations from the exploratory data analysis:

- **Gender** — ~75% of purchases are made by male users. On average, males spend more per transaction than females.
- **Gender × Marital Status** — Single men spend the most during Black Friday. Men tend to spend less after marriage, likely due to added financial responsibilities.
- **Age** — Consumers in the age group **26–35** are the most active buyers and contribute the highest total purchase amount.
- **City** — City B accounts for the highest number of transactions overall. However, City C consumers show a higher average purchase amount per transaction.
- **Stay in Current City** — People who have lived in their current city for **1 year** tend to spend the most. Newer residents buy more as they are still setting up their lives.
- **Occupation** — Occupation code significantly influences average purchase amount, with notable variation across the top 10 occupations.
- **Product Category 1** — The most dominant driver of purchase amount across all models.

---

## Data Preprocessing

- Filled missing values in `Product_Category_2` and `Product_Category_3` with `0` (indicating no sub-category)
- Encoded `Gender` as binary (M=1, F=0)
- Encoded `Age` using correct ordinal mapping (0–17 → 0, 18–25 → 1, ..., 55+ → 6) instead of alphabetical LabelEncoder
- Encoded `City_Category` as (A=0, B=1, C=2)
- One-hot encoded `Stay_In_Current_City_Years` using `pd.get_dummies`
- Dropped `User_ID` and `Product_ID` as they are not predictive features
- Performed IQR-based outlier analysis on the `Purchase` column — outliers were retained as they represent genuine high-value purchases

---

## Modeling Phase

- Dataset split into 80% train and 20% test (random_state=42)
- Four supervised regression models were trained and evaluated
- 5-fold cross-validation applied to all models for robust evaluation
- Training time recorded for each model
- Hyperparameter tuning performed on XGBoost using `RandomizedSearchCV` (20 iterations, 3-fold CV)

### Models Used

| Model | Description |
|-------|-------------|
| Linear Regression | Baseline model |
| Decision Tree Regressor | Non-linear, interpretable |
| Random Forest Regressor | Ensemble of 100 trees |
| XGBoost Regressor | Gradient boosting, best performer |

---

## Evaluation Metric

**Root Mean Square Error (RMSE)** — measures the average magnitude of prediction errors. Lower is better.

**R² Score** — measures how well the model explains variance in the target. Higher is better.

**Cross-Validation RMSE** — 5-fold CV RMSE used to check for overfitting and model stability.

**SHAP values** — used to explain feature contributions at the individual prediction level.

---

## Results

| Model | RMSE | MAE | R² |
|-------|------|-----|----|
| Linear Regression | ~4700 | ~3700 | ~0.15 |
| Decision Tree | ~3700 | ~2500 | ~0.45 |
| Random Forest | ~3050 | ~2200 | ~0.63 |
| **XGBoost** | **~2879** | **~2100** | **~0.67** |

**Top Features (consistent across all models):**
- `Product_Category_1` — most important feature
- `Occupation`
- `Age`

---

## Conclusion

XGBoost is the best-performing model with the lowest RMSE (~2879) and highest R² (~0.67). The model has been saved to `models/xgb_best_model.pkl` for reuse without retraining.

**Key improvements over the original notebook:**
- Fixed `df.corr()` error (requires `numeric_only=True` in newer pandas)
- Replaced deprecated `sns.distplot` → `sns.histplot`
- Fixed Age encoding to use correct ordinal order instead of alphabetical LabelEncoder
- Added cross-feature EDA (Gender × Marital Status, Top Occupation analysis)
- Added IQR-based outlier analysis
- Added 5-fold cross-validation and training time tracking for all models
- Added RandomizedSearchCV for XGBoost hyperparameter tuning
- Added residual plot and error distribution analysis
- Added feature importance comparison across all models side by side
- Added SHAP explainability plots (beeswarm + bar)
- Added custom prediction demo for any customer profile
- Added model saving and reloading with joblib

---

## How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/Black-Friday-Sales-Prediction.git
   cd Black-Friday-Sales-Prediction
   ```

2. Install dependencies
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn xgboost shap joblib
   ```

3. Launch the notebook
   ```bash
   jupyter notebook "Black Friday Sales Prediction.ipynb"
   ```

4. Run all cells top to bottom

> To load the saved model directly without retraining:
> ```python
> import joblib
> model = joblib.load('models/xgb_best_model.pkl')
> predictions = model.predict(X_test)
> ```

---

## Technologies Used

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-red)
![SHAP](https://img.shields.io/badge/SHAP-Explainability-purple)

- Python 3.8+
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Joblib