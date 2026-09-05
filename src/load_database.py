import sqlite3

import pandas as pd


DATABASE_PATH = "banking.db"


# Connect to SQLite
connection = sqlite3.connect(DATABASE_PATH)


# Load CSV files
customers = pd.read_csv("data/customers.csv")
accounts = pd.read_csv("data/accounts.csv")
transactions = pd.read_csv(
    "data/transactions.csv"
)


# Convert transaction date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)


# Load tables
customers.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False,
)

accounts.to_sql(
    "accounts",
    connection,
    if_exists="replace",
    index=False,
)

transactions.to_sql(
    "transactions",
    connection,
    if_exists="replace",
    index=False,
)


# Create indexes
connection.execute(
    """
    CREATE INDEX IF NOT EXISTS
    idx_transactions_account
    ON transactions(account_id)
    """
)

connection.execute(
    """
    CREATE INDEX IF NOT EXISTS
    idx_transactions_date
    ON transactions(transaction_date)
    """
)

connection.execute(
    """
    CREATE INDEX IF NOT EXISTS
    idx_transactions_fraud
    ON transactions(is_fraud)
    """
)


connection.commit()
connection.close()


print("Banking database created successfully!")
print("Database: banking.db")
print("Tables: customers, accounts, transactions")