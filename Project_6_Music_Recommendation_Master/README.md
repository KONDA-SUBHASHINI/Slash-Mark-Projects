# 🎵 Music Recommender System

A complete machine learning project that builds **three different music recommendation systems** from scratch using Python and Jupyter Notebooks. This project covers the two major types of recommender systems — **Content-Based Filtering** and **Collaborative Filtering** — and implements them using real-world techniques used in industry.

---

## 📌 What is a Recommender System?

A recommender system is a type of machine learning system that predicts what a user might like based on available data. You interact with recommender systems every day — when Spotify suggests songs, or YouTube recommends videos.

There are two main types:

| Type | How it works | Example |
|------|-------------|---------|
| **Content-Based** | Recommends items similar to what you already like, based on item features | "You liked this song's lyrics → here are songs with similar lyrics" |
| **Collaborative Filtering** | Recommends items based on what similar users liked | "Users who listened to the same songs as you also liked these" |

This project implements **both types**, giving you a full picture of how recommendation systems work.

---

## 📁 Project Structure

```
music_recommender-master/
│
├── README.md                                         # This file
├── requirements.txt                                  # Python dependencies
│
├── collaborative_recommender_system/                 # Collaborative filtering notebooks
│   ├── CF_knn_music_recommender.ipynb                # Approach 1: KNN-based
│   ├── CF_matrix_fact_music_recommender.ipynb        # Approach 2: SVD Matrix Factorization
│   └── recommeders/                                  # Helper module
│       ├── __init__.py
│       └── knn_recommender.py                        # Recommender class used by KNN notebook
│
└── content based recommedation system/               # Content-based filtering
    ├── content_based_music_recommender.ipynb         # Approach 3: TF-IDF + Cosine Similarity
    └── songdata.csv                                  # Dataset: 57,650 songs with lyrics
```

---

## 🧠 The Three Approaches Explained

### 1. 📝 Content-Based Filtering
**Notebook:** `content based recommedation system/content_based_music_recommender.ipynb`

**How it works:**
- Uses a dataset of **57,650 English songs** with lyrics (`songdata.csv`)
- Converts song lyrics into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**
- Measures similarity between songs using **Cosine Similarity**
- Recommends songs whose lyrics are most similar to the input song

**What you will see:**
- A song is picked from the dataset
- The system returns the most lyrically similar songs with similarity scores

**Best for:** Recommending songs based on lyrical content and themes

---

### 2. 🤝 Collaborative Filtering — K-Nearest Neighbors (KNN)
**Notebook:** `collaborative_recommender_system/CF_knn_music_recommender.ipynb`

**How it works:**
- Uses a **user–song interaction matrix** (who listened to what, and how many times)
- Converts it into a **sparse matrix** using `scipy` to handle memory efficiently
- Applies **K-Nearest Neighbors** to find songs that are listened to by similar users
- Uses **fuzzy matching** (via Python's `difflib`) to search for song titles with typo tolerance

**What you will see:**
- Exploratory data analysis (most popular songs, artists, listening patterns)
- A song title is entered and the system returns 10 similar songs

**Best for:** Finding songs that people with similar taste have enjoyed

---

### 3. 🔢 Collaborative Filtering — Matrix Factorization (SVD)
**Notebook:** `collaborative_recommender_system/CF_matrix_fact_music_recommender.ipynb`

**How it works:**
- Also uses the user–song interaction matrix
- Applies **SVD (Singular Value Decomposition)** via `scipy.sparse.linalg.svds`
- Breaks the large sparse matrix into smaller **latent factor matrices** representing hidden user preferences and song characteristics
- Finds the best number of latent factors using a **grid search + cross-validation**
- Evaluates model accuracy using **RMSE (Root Mean Squared Error)**

**What you will see:**
- Data preparation and sparsity analysis
- Grid search to find the best SVD parameters
- 5-fold cross-validation results
- Final RMSE score on the test set

**Best for:** Handling very large, sparse datasets; scales well to millions of users

---

## ⚙️ Installation

### Step 1 — Make sure Python is installed
You need **Python 3.8 or above**. Check with:
```bash
python --version
```

### Step 2 — Install required libraries
Open a terminal in the project folder and run:
```bash
pip install -r requirements.txt
```

This installs:
- `pandas` — data manipulation
- `numpy` — numerical computing
- `scikit-learn` — machine learning (TF-IDF, KNN, train/test split)
- `scipy` — sparse matrices and SVD
- `matplotlib` — plotting
- `seaborn` — statistical visualizations
- `jupyter` — to run the notebooks

---

## ▶️ How to Run

### Step 1 — Launch Jupyter Notebook
```bash
jupyter notebook
```
This opens a browser window showing the project folder.

### Step 2 — Open a notebook
Navigate into a folder and click on any `.ipynb` file to open it.

### Step 3 — Run the cells
- Click **"Run All"** from the Cell menu, OR
- Press **`Shift + Enter`** to run one cell at a time from top to bottom

### ✅ Recommended order to run:
1. Start with `content_based_music_recommender.ipynb` — simplest, standalone, no dependencies
2. Then `CF_knn_music_recommender.ipynb` — intermediate, uses the `recommeders/` module
3. Finally `CF_matrix_fact_music_recommender.ipynb` — most advanced, uses SVD

---

## 📊 Datasets

| Dataset | Used In | Description |
|---------|---------|-------------|
| `songdata.csv` | Content-Based notebook | 57,650 English songs with artist, title, and full lyrics. Source: Kaggle (LyricsFreak scrape) |
| Synthetic user–song data | Both Collaborative notebooks | Auto-generated inside the notebook. Simulates user listening history (500 users × 200 songs). The original Million Song Dataset URLs from `static.turi.com` are permanently offline. |

---

## 🔧 Changes & Fixes Applied

The original project had several issues that prevented it from running. All have been fixed:

| File | Problem | Fix Applied |
|------|---------|-------------|
| `knn_recommender.py` | Used `fuzzywuzzy` library which is no longer installable | Replaced with Python built-in `difflib.SequenceMatcher` — same fuzzy string matching, zero extra dependencies |
| `CF_knn_music_recommender.ipynb` | Data URLs (`static.turi.com`) permanently offline | Replaced with synthetic dataset generated inside the notebook |
| `CF_knn_music_recommender.ipynb` | `sns.distplot()` removed in seaborn 0.12+ | Replaced with `sns.histplot(kde=True)` |
| `CF_knn_music_recommender.ipynb` | `sns.barplot` palette warnings in newer seaborn | Added `hue=` and `legend=False` parameters |
| `CF_knn_music_recommender.ipynb` | `pivot()` crashed with duplicate user–song pairs | Added `groupby().sum()` aggregation before pivot |
| `CF_matrix_fact_music_recommender.ipynb` | Used `surprise` library which is not installable | Replaced entirely with `scipy.sparse.linalg.svds` with manual grid search and cross-validation |
| `CF_matrix_fact_music_recommender.ipynb` | `pd.cut()` produces Categorical dtype, causing `groupby().sum()` to fail | Added `pd.to_numeric()` conversion after `pd.cut()` |
| `CF_matrix_fact_music_recommender.ipynb` | Filter thresholds too strict for synthetic data → empty pivot | Lowered user/song filters from `>16`/`>200` to `>2` |
| `content_based_music_recommender.ipynb` | Wrong CSV path — notebook looked for file from wrong directory | Fixed path to resolve relative to the notebook's own folder |

---

## 💡 Key Concepts Glossary

| Term | Meaning |
|------|---------|
| **TF-IDF** | A scoring method that finds the most important words in a document relative to a collection |
| **Cosine Similarity** | Measures how similar two vectors are by the angle between them (1 = identical, 0 = no similarity) |
| **KNN** | K-Nearest Neighbors — finds the K most similar items to a given item |
| **Sparse Matrix** | A matrix where most values are zero — stored efficiently using special formats |
| **SVD** | Singular Value Decomposition — breaks a matrix into latent factors representing hidden patterns |
| **RMSE** | Root Mean Squared Error — measures how far predictions are from actual values (lower is better) |
| **Latent Factors** | Hidden features learned by the model (e.g., "this user likes upbeat songs") |

---

## 👤 Author
Original project: Music Recommender System using ML  
Fixed and updated for compatibility with modern Python libraries (pandas 3.x, seaborn 0.12+, scikit-learn 1.x)