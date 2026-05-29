# Project 2 - XGBoost House Price Prediction

A Machine Learning project that predicts house prices using **Linear Regression** and **XGBoost** algorithms. The model is trained on the King County House Sales dataset containing over 21,000 real house sales records from the Seattle, USA area.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Model Results](#model-results)
- [Sample Predictions](#sample-predictions)

---

## 📖 About the Project

This project builds and compares two regression models to predict house prices:
- **Linear Regression** — a simple baseline model
- **XGBoost Regressor** — an advanced gradient boosting model

Both models are trained on real house sales data and evaluated using MAE, RMSE, and R² Score. XGBoost significantly outperforms Linear Regression on this dataset.

---

## 📂 Dataset

| Property | Details |
|----------|---------|
| **File** | `kc_house_data.csv` |
| **Rows** | 21,613 house sales |
| **Columns** | 21 features |
| **Target** | `price` (house sale price in USD) |
| **Price Range** | $75,000 — $7,700,000 |
| **Average Price** | $540,088 |
| **Missing Values** | None |

### Key Features:
| Feature | Description |
|---------|-------------|
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `sqft_living` | Square footage of living area |
| `sqft_lot` | Square footage of the lot |
| `floors` | Number of floors |
| `waterfront` | Whether the house has a waterfront view |
| `grade` | Overall grade given to the housing unit |
| `condition` | Overall condition of the house |
| `yr_built` | Year the house was built |
| `zipcode` | ZIP code area |
| `lat` / `long` | Latitude and Longitude |

---

## ✨ Features

- ✅ Data loading and exploration
- ✅ Data visualizations (price distribution, bedroom count, scatter plots)
- ✅ Linear Regression model training and evaluation
- ✅ XGBoost Regressor model training and evaluation
- ✅ Model evaluation using MAE, RMSE and R² Score
- ✅ Model comparison summary

---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `pandas` — data loading and manipulation
  - `numpy` — numerical operations
  - `matplotlib` & `seaborn` — data visualization
  - `xgboost` — XGBoost regression model
  - `scikit-learn` — Linear Regression, train/test split, evaluation metrics

---

## 📁 Project Structure

```
project2/
├── housesales.ipynb      # Jupyter Notebook with full ML pipeline
├── kc_house_data.csv     # Dataset (King County house sales)
└── README.md             # Project documentation
```

---

## ✅ Prerequisites

- Python 3.x installed
- Jupyter Notebook or Jupyter Lab
- pip (Python package manager)

---

## ⚙️ Installation & Setup

**Step 1: Navigate to the project folder**
```bash
cd project2
```

**Step 2: Install required packages**
```bash
pip install pandas numpy matplotlib seaborn xgboost scikit-learn
```

**Step 3: Launch Jupyter**
```bash
jupyter notebook
```
or
```bash
jupyter lab
```

---

## ▶️ How to Run

1. Open `housesales.ipynb` in Jupyter
2. Run all cells top to bottom:
   ```
   Kernel → Restart & Run All
   ```

---

## 📊 Model Results

| Metric | Linear Regression | XGBoost |
|--------|-------------------|---------|
| **R² Score** | ~0.70 | ~0.88 |
| **MAE** | ~$125,000 | ~$67,000 |
| **RMSE** | ~$200,000 | ~$134,000 |

XGBoost explains **88% of the variance** in house prices — significantly better than Linear Regression.

---

## 🏠 Sample Predictions (XGBoost)

```
Sample    Actual Price    Predicted Price
  1        $365,000         $387,578
  2        $865,000         $878,444
  3      $1,038,000       $1,140,166
  4        $711,000         $743,314
  5        $450,000         $467,231
```

---

## 📝 Notes

- Dataset is split 80% training and 20% testing
- XGBoost hyperparameters: 500 estimators, learning rate 0.05, max depth 5
- Both models are compared side by side in the final summary cell