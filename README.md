# 🤖 Slashmark ML Internship Projects

A collection of **6 Machine Learning projects** completed as part of the Slashmark internship program. The projects span classical ML, deep learning, data engineering, and recommender systems — progressing from beginner to advanced level.

---

## 📁 Repository Structure

```
Slashmark-ML-Projects/
│
├── Project_1_Task_Management_App/
│   ├── main.py
│   ├── tasks.csv
│   ├── requirements.txt
│   ├── instructions.txt
│   └── README.md
│
├── Project_2_House_Price_Prediction/
│   ├── housesales.ipynb
│   ├── kc_house_data.csv
│   └── README.md
│
├── Project_3_Handwritten_Digit_Recognition/
│   ├── 1. K Nearest Neighbors/
│   ├── 2. SVM/
│   ├── 3. Random Forest Classifier/
│   ├── CNN_Keras/
│   ├── Outputs/
│   ├── Results/
│   ├── download_dataset.py
│   ├── requirements.txt
│   └── README.md
│
├── Project_4_Blood_Donation_Forecast/
│   ├── datasets/
│   │   └── transfusion.data
│   ├── notebook.ipynb
│   └── README.md
│
├── Project_5_Black_Friday_Sales_Prediction/
│   ├── Data/
│   │   └── BlackFridaySales.csv
│   ├── models/
│   │   └── xgb_best_model.pkl
│   ├── Black Friday Sales Prediction.ipynb
│   └── README.md
│
└── Project_6_Music_Recommender_System/
    ├── collaborative_recommender_system/
    │   ├── CF_knn_music_recommender.ipynb
    │   ├── CF_matrix_fact_music_recommender.ipynb
    │   └── recommeders/
    ├── content based recommedation system/
    │   ├── content_based_music_recommender.ipynb
    │   └── songdata.csv
    ├── requirements.txt
    └── README.md
```

---

## 📋 Projects Overview

| # | Project | Type | Algorithm(s) | Key Metric |
|---|---------|------|-------------|------------|
| 1 | Task Management App | CLI App | Naive Bayes (priority classifier) | Rule-based recommendation |
| 2 | House Price Prediction | Regression | Linear Regression, XGBoost | R² = 0.88 (XGBoost) |
| 3 | Handwritten Digit Recognition | Classification | KNN, SVM, Random Forest, CNN | 99.31% accuracy (CNN) |
| 4 | Blood Donation Forecast | Binary Classification | Logistic Regression, Random Forest | AUC = 0.7577 |
| 5 | Black Friday Sales Prediction | Regression | Linear Regression, Decision Tree, Random Forest, XGBoost | RMSE ≈ 2879 (XGBoost) |
| 6 | Music Recommender System | Recommender System | TF-IDF + Cosine Similarity, KNN, SVD | 3 recommendation approaches |

---

## 🗂️ Project Details

---

### Project 1 — Simple Task Management App

A command-line Python application to manage daily tasks with smart priority-based recommendations. Tasks are saved persistently in a CSV file.

**Features:** Add, remove, list tasks · Priority levels (Low / Medium / High) · Smart recommendation (always suggests highest priority task first) · Persistent CSV storage

**Tech Stack:** Python · pandas · scikit-learn (Naive Bayes)

**How to Run:**
```bash
cd Project_1_Task_Management_App
pip install pandas scikit-learn
python main.py
```

---

### Project 2 — XGBoost House Price Prediction

Predicts house prices using the King County House Sales dataset (21,613 records). Compares Linear Regression and XGBoost.

**Results:**

| Metric | Linear Regression | XGBoost |
|--------|-------------------|---------|
| R² Score | ~0.70 | ~0.88 |
| MAE | ~$125,000 | ~$67,000 |
| RMSE | ~$200,000 | ~$134,000 |

**Tech Stack:** Python · pandas · numpy · matplotlib · seaborn · scikit-learn · XGBoost

**How to Run:**
```bash
cd Project_2_House_Price_Prediction
pip install pandas numpy matplotlib seaborn xgboost scikit-learn
jupyter notebook housesales.ipynb
```

---

### Project 3 — Handwritten Digit Recognition

Trains and compares four models on the MNIST dataset (70,000 images, 28×28 pixels).

**Results:**

| Algorithm | Test Accuracy |
|-----------|--------------|
| K Nearest Neighbors | 96.81% |
| Support Vector Machine | 97.64% |
| Random Forest | 96.89% |
| **CNN (Deep Learning)** | **99.31%** |

**Tech Stack:** Python · scikit-learn · TensorFlow · Keras · OpenCV · NumPy · Matplotlib

**How to Run:**
```bash
cd Project_3_Handwritten_Digit_Recognition
pip install -r requirements.txt
python download_dataset.py       # downloads MNIST for KNN/SVM/RFC
cd "1. K Nearest Neighbors" && python knn.py
cd "../2. SVM" && python svm.py
cd "../3. Random Forest Classifier" && python RFC.py
cd "../CNN_Keras" && python CNN_MNIST.py
```

---

### Project 4 — Blood Donation Forecast

Binary classification to predict whether a blood donor will donate again, using real donor data from Taiwan (748 records, 533 after deduplication).

**Results:**

| Model | AUC-ROC |
|-------|---------|
| Logistic Regression (baseline) | 0.7527 |
| Log-normalized Monetary | 0.7533 |
| **StandardScaler Pipeline** | **0.7577** |
| Random Forest | 0.6102 |
| CV Mean (5-fold) | 0.7399 ± 0.0402 |

**Key Finding:** 215 duplicate rows (28.7%) were found and removed before modelling — this significantly improved donor recall from 11% to 35%.

**Tech Stack:** Python · pandas · numpy · scikit-learn

**How to Run:**
```bash
cd Project_4_Blood_Donation_Forecast
pip install pandas numpy scikit-learn jupyter
jupyter notebook notebook.ipynb
```

---

### Project 5 — Black Friday Sales Prediction

Regression task to predict customer purchase amounts from 550,068 Black Friday transaction records. Includes EDA, outlier analysis, SHAP explainability, and hyperparameter tuning.

**Results:**

| Model | RMSE | R² |
|-------|------|----|
| Linear Regression | ~4700 | ~0.15 |
| Decision Tree | ~3700 | ~0.45 |
| Random Forest | ~3050 | ~0.63 |
| **XGBoost** | **~2879** | **~0.67** |

**Top Features:** `Product_Category_1` · `Occupation` · `Age`

**Tech Stack:** Python · pandas · numpy · matplotlib · seaborn · scikit-learn · XGBoost · SHAP · joblib

**How to Run:**
```bash
cd Project_5_Black_Friday_Sales_Prediction
pip install numpy pandas matplotlib seaborn scikit-learn xgboost shap joblib
jupyter notebook "Black Friday Sales Prediction.ipynb"
```

---

### Project 6 — Music Recommender System

Implements three music recommendation approaches covering both Content-Based and Collaborative Filtering.

| Approach | Notebook | Method |
|----------|----------|--------|
| Content-Based | `content_based_music_recommender.ipynb` | TF-IDF + Cosine Similarity on 57,650 song lyrics |
| Collaborative — KNN | `CF_knn_music_recommender.ipynb` | Sparse matrix + K-Nearest Neighbors + fuzzy matching |
| Collaborative — SVD | `CF_matrix_fact_music_recommender.ipynb` | Matrix Factorization via SVD + grid search + 5-fold CV |

**Tech Stack:** Python · pandas · numpy · scikit-learn · scipy · matplotlib · seaborn · jupyter

**How to Run:**
```bash
cd Project_6_Music_Recommender_System
pip install -r requirements.txt
jupyter notebook
```
Run notebooks in this order:
1. `content_based_music_recommender.ipynb`
2. `CF_knn_music_recommender.ipynb`
3. `CF_matrix_fact_music_recommender.ipynb`

---

## ⚙️ Global Setup

**Python version required:** 3.8 or above

```bash
python --version       # verify Python is installed
pip install jupyter    # if Jupyter is not installed
```

Clone the repository:
```bash
git clone https://github.com/KONDA-SUBHASHINI/Slash-Mark-ML-Projects.git
cd Slash-Mark-ML-Projects
```

Each project has its own `requirements.txt` or install instructions in its README. Install dependencies per project as shown above.

---

## 🧠 Key Learnings Across Projects

- **Data cleaning is critical** — duplicate removal (Project 4), missing value handling (Project 5), and correct label encoding (Project 5) all had major impact on results
- **Evaluation metric choice matters** — AUC-ROC over accuracy for imbalanced datasets (Project 4); RMSE for regression (Projects 2, 5)
- **Feature scaling** is essential for linear models — a single high-variance feature can blind the model (Project 4)
- **Ensemble methods beat baselines** — XGBoost outperformed Linear Regression in both Projects 2 and 5
- **Deep learning dominates image tasks** — CNN achieved 99.31% vs 97.64% for the best classical ML model (Project 3)
- **Library compatibility** matters in production — fixed `fuzzywuzzy`, `surprise`, deprecated seaborn functions, and broken data URLs across Project 6

---

## 👤 Author

**Konda Subhashini**
Slashmark ML Internship
GitHub: [KONDA-SUBHASHINI](https://github.com/KONDA-SUBHASHINI/Slash-Mark-ML-Projects)
