-- ============================================
-- BANKING TRANSACTION & FRAUD ANALYTICS
-- SQL ANALYSIS
-- ============================================


-- 1. Total number of customers

SELECT COUNT(*) AS total_customers
FROM customers;


-- 2. Total number of accounts

SELECT COUNT(*) AS total_accounts
FROM accounts;


-- 3. Total transactions

SELECT COUNT(*) AS total_transactions
FROM transactions;


-- 4. Total transaction amount

SELECT
    ROUND(SUM(amount), 2) AS total_transaction_amount
FROM transactions;


-- 5. Average transaction amount

SELECT
    ROUND(AVG(amount), 2) AS average_transaction_amount
FROM transactions;


-- 6. Transaction count by transaction type

SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- 7. Transaction count by channel

SELECT
    channel,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY channel
ORDER BY transaction_count DESC;


-- 8. Transaction count by location

SELECT
    location,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY location
ORDER BY total_amount DESC;


-- 9. Fraud vs non-fraud transactions

SELECT
    is_fraud,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY is_fraud;


-- 10. Fraud percentage

SELECT
    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_percentage
FROM transactions;


-- 11. Average amount of fraudulent transactions

SELECT
    ROUND(AVG(amount), 2) AS average_fraud_amount
FROM transactions
WHERE is_fraud = 1;


-- 12. Top 10 accounts by transaction amount

SELECT
    account_id,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY account_id
ORDER BY total_amount DESC
LIMIT 10;


-- 13. Customer transaction analysis

SELECT
    c.customer_id,
    c.age,
    c.gender,
    c.city,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_transaction_amount
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY
    c.customer_id,
    c.age,
    c.gender,
    c.city
ORDER BY total_transaction_amount DESC
LIMIT 10;


-- 14. Fraud transactions by location

SELECT
    location,
    COUNT(*) AS fraud_transactions,
    ROUND(SUM(amount), 2) AS fraud_amount
FROM transactions
WHERE is_fraud = 1
GROUP BY location
ORDER BY fraud_transactions DESC;


-- 15. Fraud transactions by channel

SELECT
    channel,
    COUNT(*) AS fraud_transactions,
    ROUND(SUM(amount), 2) AS fraud_amount
FROM transactions
WHERE is_fraud = 1
GROUP BY channel
ORDER BY fraud_transactions DESC;


-- 16. Large transactions

SELECT
    transaction_id,
    account_id,
    transaction_date,
    amount,
    merchant,
    location,
    channel,
    is_fraud
FROM transactions
WHERE amount > 10000
ORDER BY amount DESC;


-- 17. Fraudulent large transactions

SELECT
    transaction_id,
    account_id,
    transaction_date,
    amount,
    merchant,
    location,
    channel
FROM transactions
WHERE amount > 10000
  AND is_fraud = 1
ORDER BY amount DESC;