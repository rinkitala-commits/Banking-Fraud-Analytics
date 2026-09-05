import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# Reproducibility
random.seed(42)
np.random.seed(42)


# -----------------------------
# Configuration
# -----------------------------
NUM_CUSTOMERS = 1000
NUM_TRANSACTIONS = 20000

TRANSACTION_TYPES = [
    "Purchase",
    "Withdrawal",
    "Transfer",
    "Payment",
    "Deposit",
]

CHANNELS = [
    "ATM",
    "Online",
    "Mobile",
    "Branch",
    "POS",
]

LOCATIONS = [
    "Kolkata",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Ahmedabad",
]

MERCHANTS = [
    "Amazon",
    "Flipkart",
    "Walmart",
    "Swiggy",
    "Zomato",
    "Uber",
    "BookMyShow",
    "Myntra",
    "Reliance",
    "DMart",
    "Local Store",
    "Electronics Store",
    "Travel Agency",
]


# -----------------------------
# Generate customers
# -----------------------------
customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    age = random.randint(18, 75)

    customers.append(
        {
            "customer_id": customer_id,
            "age": age,
            "gender": random.choice(["Male", "Female"]),
            "city": random.choice(LOCATIONS),
        }
    )

customers_df = pd.DataFrame(customers)


# -----------------------------
# Generate accounts
# -----------------------------
accounts = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    accounts.append(
        {
            "account_id": f"ACC{customer_id:05d}",
            "customer_id": customer_id,
            "account_type": random.choice(
                ["Savings", "Current"]
            ),
        }
    )

accounts_df = pd.DataFrame(accounts)


# -----------------------------
# Generate transactions
# -----------------------------
transactions = []

start_date = datetime(2025, 1, 1)

for transaction_id in range(1, NUM_TRANSACTIONS + 1):

    account = random.choice(accounts)

    transaction_date = start_date + timedelta(
        days=random.randint(0, 364),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
    )

    transaction_type = random.choice(TRANSACTION_TYPES)

    # Normal transaction amount
    amount = round(
        np.random.lognormal(mean=5.2, sigma=1.0),
        2,
    )

    amount = min(amount, 100000)

    channel = random.choice(CHANNELS)
    location = random.choice(LOCATIONS)
    merchant = random.choice(MERCHANTS)

    # -----------------------------
    # Fraud generation
    # -----------------------------
    fraud_probability = 0.015

    # Large transactions are more suspicious
    if amount > 10000:
        fraud_probability += 0.10

    if amount > 25000:
        fraud_probability += 0.15

    # Online/mobile transactions have slightly higher risk
    if channel in ["Online", "Mobile"]:
        fraud_probability += 0.02

    is_fraud = int(
        random.random() < fraud_probability
    )

    transactions.append(
        {
            "transaction_id": transaction_id,
            "account_id": account["account_id"],
            "transaction_date": transaction_date,
            "transaction_type": transaction_type,
            "amount": amount,
            "merchant": merchant,
            "location": location,
            "channel": channel,
            "is_fraud": is_fraud,
        }
    )


transactions_df = pd.DataFrame(transactions)


# -----------------------------
# Save datasets
# -----------------------------
customers_df.to_csv(
    "data/customers.csv",
    index=False,
)

accounts_df.to_csv(
    "data/accounts.csv",
    index=False,
)

transactions_df.to_csv(
    "data/transactions.csv",
    index=False,
)


# -----------------------------
# Summary
# -----------------------------
print("Banking dataset generated successfully!")
print()
print(f"Customers: {len(customers_df):,}")
print(f"Accounts: {len(accounts_df):,}")
print(f"Transactions: {len(transactions_df):,}")
print()
print("Fraud distribution:")
print(transactions_df["is_fraud"].value_counts())
print()
print("Files created:")
print("data/customers.csv")
print("data/accounts.csv")
print("data/transactions.csv")