# 🏦 Banking Transaction & Fraud Analytics

A complete end-to-end data analytics and machine learning project that analyzes banking transactions, identifies fraud patterns, performs advanced SQL analysis, and predicts potential fraudulent transactions using machine learning.

> **Note:** This project uses a synthetic banking transaction dataset created for educational and portfolio purposes. It does not represent real customer banking data.

---

## 🚀 Project Overview

The project simulates a real-world banking analytics workflow:

```text
Banking Transactions
        ↓
Data Storage & SQL
        ↓
SQL Business Analysis
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Machine Learning
        ↓
Fraud Prediction
        ↓
Interactive Streamlit Dashboard
```

The project combines:

- SQL
- Python
- Pandas
- NumPy
- Data Visualization
- Exploratory Data Analysis
- Machine Learning
- Streamlit
- SQLite

## 🎯 Business Problem

Banks process thousands or millions of transactions every day.

The analytics team needs to answer questions such as:

- How many transactions are being processed?
- What is the total transaction value?
- Which channels have the highest fraud rate?
- Which locations have more fraudulent activity?
- Which transaction types are associated with higher fraud rates?
- What customers have unusual transaction behavior?
- Can machine learning identify potentially fraudulent transactions?

This project attempts to answer these questions using SQL, data analysis, and machine learning.

## 📊 Key Analytics

**The project performs analysis including:**

- Transaction Analytics
- Total transaction volume
- Total transaction value
- Average transaction amount
- Transaction distribution
- Transaction types
- Transaction channels
- Geographic transaction patterns
- Fraud Analytics
- Fraud vs non-fraud transactions
- Overall fraud percentage
- Fraud rate by channel
- Fraud rate by transaction type
- Fraud rate by location
- Fraudulent transaction amounts
- Monthly fraud trends
- Daily fraud activity
- High-risk transactions
- Customer Analytics
- Customer transaction volume
- Customer transaction value
- Customer fraud count
- Customer fraud rate
- High-value customers
- Customer ranking using SQL window functions

## 🧮 SQL Analysis

The project uses SQLite for relational data analysis.

**SQL techniques include:**

SELECT
WHERE
GROUP BY
ORDER BY
HAVING
INNER JOIN
CASE statements
Common Table Expressions (CTEs)
Window Functions
RANK()
Date-based analysis
Aggregations

**Example relationship:**

```text
Customers
    │
    │ customer_id
    ↓
Accounts
    │
    │ account_id
    ↓
Transactions
```

## 🔍 Exploratory Data Analysis

Python is used to investigate transaction behavior and fraud patterns.

### EDA includes:

- ata quality checks
- Missing-value analysis
- Transaction distributions
- Fraud distribution
- Channel analysis
- Location analysis
- Transaction type analysis
- Transaction amount analysis
- Time-based fraud analysis
- Correlation analysis

## ⚙️ Feature Engineering

The following features are created from transaction data:

hour
day_of_week
day_of_month
month
is_weekend
is_high_value

### Categorical features include:

transaction_type
channel
location
merchant

Categorical variables are transformed using One-Hot Encoding.

## 🤖 Machine Learning

Two classification models are implemented:

- Logistic Regression

- Used as an interpretable baseline classification model.

- Random Forest

- Used to capture nonlinear relationships and interactions between transaction features.

### Both models use:

- Class-weight balancing
- Train/Test Split
- One-Hot Encoding
- Missing-value handling
- Pipeline-based preprocessing

## 📈 Model Evaluation

The models are evaluated using:

-Accuracy

- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

For fraud detection, recall is particularly important because failing to identify fraudulent transactions can have significant consequences.

The final model selection should consider the business trade-off between:

False Positives
vs
False Negatives

## 📊 Feature Importance

Random Forest feature importance is analyzed to understand which variables contribute most strongly to the model's predictions.

This improves model interpretability and helps identify potentially useful fraud indicators.

## 🖥️ Interactive Dashboard

The project includes a Streamlit dashboard providing:

- KPI Dashboard
- Total Transactions
- Total Transaction Amount
- Fraud Transactions
- Fraud Rate
- Interactive Analysis
- Transaction channel analysis
- Transaction type analysis
- Fraud by channel
- Fraud by location
- Monthly fraud trends
- High-risk transactions
- Fraud Prediction

Users can enter transaction details and receive:

Fraud Probability +
Risk Classification

## 📁 Project Structure

```text
Banking-Fraud-Analytics/
│
├── data/
│ ├── customers.csv
│ ├── accounts.csv
│ └── transactions.csv
│
├── sql/
│ ├── analysis.sql
│ └── advanced_analysis.sql
│
├── models/
│ ├── train_model.py
│ └── model_results.csv
│
├── notebooks/
│ └── 01_banking_eda.ipynb
│
├── dashboard/
│ └── app.py
│
├── src/
│ ├── run_sql.py
│ └── run_advanced_sql.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Technologies

Category Technologies

**Programming**

- Python

**Database**

- SQLite

**SQL**

- SQL

**Data Analysis**

- Pandas, NumPy

**Visualization**

- Matplotlib, Seaborn

**Machine Learning**

- Scikit-learn

**Dashboard**

- Streamlit

**Notebook**

- Jupyter

**Model Persistence**

- Joblib

**Version Control**

- Git, GitHub

## ▶️ How to Run

1. Clone the repository

```bash
  git clone (https://github.com/rinkitala-commits/Banking-Fraud-Analytics)
```

2. Navigate into the project

```bash
   cd Banking-Fraud-Analytics
```

3. Create a virtual environment

```bash
   python -m venv .venv
```

4. Activate the environment

```bash
Windows PowerShell:
.venv\Scripts\Activate.ps1
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Run SQL analysis

```bash
python src/run_sql.py
```

Advanced SQL:

```bash
python src/run_advanced_sql.py
```

7. Run machine learning

```bash
python models/train_model.py
```

8. Launch dashboard

```bash
streamlit run dashboard/app.py
```

## 📌 Skills Demonstrated

This project demonstrates practical skills in:

SQL

- Relational database analysis
- Joins
- Aggregations
- CTEs
- Window functions
- Business analytics
- Data Analysis
- Data cleaning
- Exploratory analysis
- Statistical summaries
- Pattern identification
- Time-series analysis
- Data visualization
- Machine Learning
- Classification
- Feature engineering
- Imbalanced classification
- Model comparison
- Model evaluation
- Feature importance
- Data Applications
- Streamlit dashboards
- Interactive filtering
- ML prediction interface

## ⚠️ Dataset Disclaimer

This project uses synthetic banking transaction data.

It is intended for:

Educational purposes

- Portfolio demonstration
- SQL practice
- Data analysis practice
- Machine learning experimentation
- It should not be used to make real financial or banking decisions.

## 👩‍💻 Author

**Jhumarani Tala**

B.Tech Data Science Student
Python Developer | Data Analyst | Data Science Enthusiast
