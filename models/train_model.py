import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split


# ============================================
# Load data
# ============================================

df = pd.read_csv(
    "data/transactions.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)


# ============================================
# Feature engineering
# ============================================

df["hour"] = df[
    "transaction_date"
].dt.hour

df["day_of_week"] = df[
    "transaction_date"
].dt.dayofweek

df["day_of_month"] = df[
    "transaction_date"
].dt.day

df["month"] = df[
    "transaction_date"
].dt.month

df["is_weekend"] = (
    df["day_of_week"] >= 5
).astype(int)

df["is_high_value"] = (
    df["amount"] >= 10000
).astype(int)


# ============================================
# Features and target
# ============================================

numeric_features = [
    "amount",
    "hour",
    "day_of_week",
    "day_of_month",
    "month",
    "is_weekend",
    "is_high_value",
]

categorical_features = [
    "transaction_type",
    "channel",
    "location",
    "merchant",
]

features = (
    numeric_features +
    categorical_features
)

X = df[features]
y = df["is_fraud"]


# ============================================
# Train / Test split
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


# ============================================
# Preprocessing
# ============================================

numeric_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="median"
            ),
        )
    ]
)

categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="most_frequent"
            ),
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
        ),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_transformer,
            numeric_features,
        ),
        (
            "categorical",
            categorical_transformer,
            categorical_features,
        ),
    ]
)


# ============================================
# Models
# ============================================

logistic_model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor,
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ]
)


random_forest_model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor,
        ),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=200,
                max_depth=12,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]
)


# ============================================
# Train models
# ============================================

print("Training Logistic Regression...")
logistic_model.fit(
    X_train,
    y_train,
)

print("Training Random Forest...")
random_forest_model.fit(
    X_train,
    y_train,
)


# ============================================
# Evaluation function
# ============================================

def evaluate_model(
    model,
    name,
):
    predictions = model.predict(
        X_test
    )

    probabilities = model.predict_proba(
        X_test
    )[:, 1]

    results = {
        "Model": name,
        "Accuracy": accuracy_score(
            y_test,
            predictions,
        ),
        "Precision": precision_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "Recall": recall_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "F1 Score": f1_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "ROC-AUC": roc_auc_score(
            y_test,
            probabilities,
        ),
    }

    return results


# ============================================
# Compare models
# ============================================

results = [
    evaluate_model(
        logistic_model,
        "Logistic Regression",
    ),
    evaluate_model(
        random_forest_model,
        "Random Forest",
    ),
]

results_df = pd.DataFrame(results)

print("\nModel Performance")
print("=" * 70)

print(
    results_df.round(4).to_string(
        index=False
    )
)


# ============================================
# Save models
# ============================================

joblib.dump(
    logistic_model,
    "models/logistic_regression.pkl",
)

joblib.dump(
    random_forest_model,
    "models/random_forest.pkl",
)

results_df.to_csv(
    "models/model_results.csv",
    index=False,
)


print("\nModels saved successfully!")
print("models/logistic_regression.pkl")
print("models/random_forest.pkl")
print("models/model_results.csv")