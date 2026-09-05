import pandas as pd


# Load datasets
customers = pd.read_csv("data/customers.csv")
accounts = pd.read_csv("data/accounts.csv")
transactions = pd.read_csv("data/transactions.csv")


print("=" * 60)
print("BANKING DATASET INSPECTION")
print("=" * 60)


# Dataset sizes
print("\nDataset Sizes:")
print(f"Customers:     {customers.shape}")
print(f"Accounts:      {accounts.shape}")
print(f"Transactions:  {transactions.shape}")


# First few rows
print("\nCustomers:")
print(customers.head())


print("\nAccounts:")
print(accounts.head())


print("\nTransactions:")
print(transactions.head())


# Missing values
print("\nMissing Values:")
print("\nCustomers:")
print(customers.isnull().sum())

print("\nAccounts:")
print(accounts.isnull().sum())

print("\nTransactions:")
print(transactions.isnull().sum())


# Fraud distribution
print("\nFraud Distribution:")
print(transactions["is_fraud"].value_counts())

print("\nFraud Percentage:")
print(
    transactions["is_fraud"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


# Transaction statistics
print("\nTransaction Amount Statistics:")
print(transactions["amount"].describe())


print("\nTransaction Types:")
print(transactions["transaction_type"].value_counts())


print("\nTransaction Channels:")
print(transactions["channel"].value_counts())


print("\nTransaction Locations:")
print(transactions["location"].value_counts())


print("\nInspection completed successfully.")