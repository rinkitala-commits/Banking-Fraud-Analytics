-- ============================================
-- BANKING TRANSACTION & FRAUD ANALYTICS
-- Database Schema
-- ============================================


-- ============================================
-- Customers
-- ============================================

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    gender VARCHAR(20),
    city VARCHAR(100)
);


-- ============================================
-- Accounts
-- ============================================

CREATE TABLE IF NOT EXISTS accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    account_type VARCHAR(50),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- ============================================
-- Transactions
-- ============================================

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id VARCHAR(20) NOT NULL,
    transaction_date DATETIME NOT NULL,
    transaction_type VARCHAR(50),
    amount DECIMAL(12, 2),
    merchant VARCHAR(100),
    location VARCHAR(100),
    channel VARCHAR(50),
    is_fraud INTEGER DEFAULT 0,

    FOREIGN KEY (account_id)
        REFERENCES accounts(account_id)
);


-- ============================================
-- Useful indexes
-- ============================================

CREATE INDEX IF NOT EXISTS idx_transactions_account
ON transactions(account_id);


CREATE INDEX IF NOT EXISTS idx_transactions_date
ON transactions(transaction_date);


CREATE INDEX IF NOT EXISTS idx_transactions_fraud
ON transactions(is_fraud);


CREATE INDEX IF NOT EXISTS idx_accounts_customer
ON accounts(customer_id);