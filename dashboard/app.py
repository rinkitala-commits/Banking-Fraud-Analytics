import sqlite3

import joblib
import pandas as pd
import streamlit as st


# ============================================
# Page configuration
# ============================================

st.set_page_config(
    page_title="Banking Fraud Analytics",
    page_icon="🏦",
    layout="wide",
)


# ============================================
# Load database
# ============================================

@st.cache_data
def load_transactions():

    connection = sqlite3.connect(
        "banking.db"
    )

    query = """
        SELECT
            t.*,
            a.customer_id,
            c.age,
            c.gender,
            c.city
        FROM transactions t
        JOIN accounts a
            ON t.account_id = a.account_id
        JOIN customers c
            ON a.customer_id = c.customer_id
    """

    df = pd.read_sql_query(
        query,
        connection,
    )

    connection.close()

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"]
    )

    return df


# ============================================
# Load model
# ============================================

@st.cache_resource
def load_model():

    return joblib.load(
        "models/random_forest.pkl"
    )


df = load_transactions()
model = load_model()


# ============================================
# Title
# ============================================

st.title(
    "🏦 Banking Transaction & Fraud Analytics"
)

st.markdown(
    """
    **SQL + Data Analysis + Machine Learning Dashboard**

    Explore banking transaction behavior,
    fraud patterns, customer risk, and
    machine-learning predictions.
    """
)


# ============================================
# Sidebar filters
# ============================================

st.sidebar.header("Filters")


locations = sorted(
    df["location"].unique()
)

selected_locations = st.sidebar.multiselect(
    "Location",
    locations,
    default=locations,
)


channels = sorted(
    df["channel"].unique()
)

selected_channels = st.sidebar.multiselect(
    "Channel",
    channels,
    default=channels,
)


# Apply filters
filtered_df = df[
    df["location"].isin(
        selected_locations
    )
    &
    df["channel"].isin(
        selected_channels
    )
]


# ============================================
# KPI metrics
# ============================================

total_transactions = len(
    filtered_df
)

total_amount = filtered_df[
    "amount"
].sum()

fraud_transactions = filtered_df[
    "is_fraud"
].sum()

fraud_rate = (
    fraud_transactions
    / total_transactions
    * 100
    if total_transactions > 0
    else 0
)


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Transactions",
    f"{total_transactions:,}",
)

col2.metric(
    "Transaction Amount",
    f"₹{total_amount:,.2f}",
)

col3.metric(
    "Fraud Transactions",
    f"{fraud_transactions:,}",
)

col4.metric(
    "Fraud Rate",
    f"{fraud_rate:.2f}%",
)


st.divider()


# ============================================
# Transaction analysis
# ============================================

st.subheader(
    "📊 Transaction Analysis"
)


col1, col2 = st.columns(2)


with col1:

    channel_data = (
        filtered_df
        .groupby("channel")
        .size()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        channel_data
    )


with col2:

    type_data = (
        filtered_df
        .groupby("transaction_type")
        .size()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        type_data
    )


# ============================================
# Fraud analysis
# ============================================

st.subheader(
    "🚨 Fraud Analysis"
)


col1, col2 = st.columns(2)


with col1:

    fraud_by_channel = (
        filtered_df
        .groupby("channel")[
            "is_fraud"
        ]
        .mean()
        .mul(100)
        .round(2)
    )

    st.write(
        "Fraud Rate by Channel (%)"
    )

    st.bar_chart(
        fraud_by_channel
    )


with col2:

    fraud_by_location = (
        filtered_df
        .groupby("location")[
            "is_fraud"
        ]
        .mean()
        .mul(100)
        .round(2)
    )

    st.write(
        "Fraud Rate by Location (%)"
    )

    st.bar_chart(
        fraud_by_location
    )


# ============================================
# Monthly fraud trend
# ============================================

st.subheader(
    "📈 Monthly Fraud Trend"
)


filtered_df["month"] = (
    filtered_df["transaction_date"]
    .dt.to_period("M")
    .astype(str)
)


monthly_fraud = (
    filtered_df
    .groupby("month")
    .agg(
        transactions=(
            "transaction_id",
            "count",
        ),
        fraud=(
            "is_fraud",
            "sum",
        ),
    )
)

st.line_chart(
    monthly_fraud
)


# ============================================
# High-risk transactions
# ============================================

st.subheader(
    "⚠️ High-Risk Transactions"
)


high_risk = filtered_df[
    (
        filtered_df["is_fraud"] == 1
    )
    |
    (
        filtered_df["amount"] >= 10000
    )
].copy()


high_risk = high_risk.sort_values(
    "amount",
    ascending=False,
)


st.dataframe(
    high_risk[
        [
            "transaction_id",
            "account_id",
            "transaction_date",
            "amount",
            "transaction_type",
            "merchant",
            "location",
            "channel",
            "is_fraud",
        ]
    ].head(50),
    use_container_width=True,
)
# ============================================
# Fraud Prediction
# ============================================

st.divider()

st.subheader(
    "🤖 Fraud Prediction"
)

st.write(
    "Enter transaction details to estimate "
    "the probability of fraud."
)


col1, col2, col3 = st.columns(3)


with col1:

    prediction_amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=1.0,
        value=5000.0,
        step=100.0,
    )

    prediction_type = st.selectbox(
        "Transaction Type",
        sorted(
            df["transaction_type"]
            .unique()
        ),
    )


with col2:

    prediction_channel = st.selectbox(
        "Channel",
        sorted(
            df["channel"].unique()
        ),
    )

    prediction_location = st.selectbox(
        "Location",
        sorted(
            df["location"].unique()
        ),
    )


with col3:

    prediction_merchant = st.selectbox(
        "Merchant",
        sorted(
            df["merchant"].unique()
        ),
    )

    prediction_hour = st.slider(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        value=12,
    )


if st.button(
    "🔍 Predict Fraud Risk"
):

    prediction_data = pd.DataFrame(
        {
            "amount": [
                prediction_amount
            ],
            "hour": [
                prediction_hour
            ],
            "day_of_week": [
                2
            ],
            "day_of_month": [
                15
            ],
            "month": [
                6
            ],
            "is_weekend": [
                0
            ],
            "is_high_value": [
                int(
                    prediction_amount >= 10000
                )
            ],
            "transaction_type": [
                prediction_type
            ],
            "channel": [
                prediction_channel
            ],
            "location": [
                prediction_location
            ],
            "merchant": [
                prediction_merchant
            ],
        }
    )

    probability = model.predict_proba(
        prediction_data
    )[0][1]

    prediction = int(
        probability >= 0.5
    )


    st.subheader(
        "Prediction Result"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Fraud Probability",
            f"{probability * 100:.2f}%",
        )


    with col2:

        if prediction == 1:

            st.error(
                "⚠️ High Fraud Risk"
            )

        else:

            st.success(
                "✅ Low Fraud Risk"
            )

# ============================================
# Footer
# ============================================

st.divider()

st.caption(
    "Banking Transaction & Fraud Analytics | "
    "Synthetic dataset for educational purposes"
)