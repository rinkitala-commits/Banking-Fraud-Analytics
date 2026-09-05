-- ============================================
-- ADVANCED BANKING FRAUD ANALYSIS
-- ============================================


-- 1. Monthly transaction volume
-- --------------------------------------------

SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY month
ORDER BY month;


-- 2. Monthly fraud analysis
-- --------------------------------------------

SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_percentage
FROM transactions
GROUP BY month
ORDER BY month;


-- 3. Fraud rate by transaction type
-- --------------------------------------------

SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_rate
FROM transactions
GROUP BY transaction_type
ORDER BY fraud_rate DESC;


-- 4. Fraud rate by channel
-- --------------------------------------------

SELECT
    channel,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_rate
FROM transactions
GROUP BY channel
ORDER BY fraud_rate DESC;


-- 5. Fraud rate by location
-- --------------------------------------------

SELECT
    location,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_rate
FROM transactions
GROUP BY location
ORDER BY fraud_rate DESC;


-- 6. Customer transaction risk profile
-- --------------------------------------------

SELECT
    c.customer_id,
    c.age,
    c.gender,
    c.city,

    COUNT(t.transaction_id)
        AS transaction_count,

    ROUND(SUM(t.amount), 2)
        AS total_transaction_amount,

    SUM(t.is_fraud)
        AS fraud_count,

    ROUND(
        100.0 * SUM(t.is_fraud)
        / COUNT(t.transaction_id),
        2
    ) AS fraud_rate

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

HAVING transaction_count >= 5

ORDER BY fraud_rate DESC;


-- 7. High-value customers
-- --------------------------------------------

SELECT
    c.customer_id,
    c.city,

    COUNT(t.transaction_id)
        AS transaction_count,

    ROUND(SUM(t.amount), 2)
        AS total_transaction_amount

FROM customers c

JOIN accounts a
    ON c.customer_id = a.customer_id

JOIN transactions t
    ON a.account_id = t.account_id

GROUP BY
    c.customer_id,
    c.city

ORDER BY total_transaction_amount DESC

LIMIT 20;


-- 8. High-risk transactions
-- --------------------------------------------

SELECT
    transaction_id,
    account_id,
    transaction_date,
    amount,
    channel,
    location,
    is_fraud,

    CASE
        WHEN amount >= 25000 THEN 'Very High'
        WHEN amount >= 10000 THEN 'High'
        WHEN amount >= 5000 THEN 'Medium'
        ELSE 'Low'
    END AS transaction_risk

FROM transactions

ORDER BY amount DESC;


-- 9. Fraud amount by risk category
-- --------------------------------------------

SELECT

    CASE
        WHEN amount >= 25000 THEN 'Very High'
        WHEN amount >= 10000 THEN 'High'
        WHEN amount >= 5000 THEN 'Medium'
        ELSE 'Low'
    END AS risk_category,

    COUNT(*) AS transaction_count,

    SUM(is_fraud) AS fraud_count,

    ROUND(SUM(amount), 2)
        AS total_transaction_amount,

    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_rate

FROM transactions

GROUP BY risk_category

ORDER BY fraud_rate DESC;


-- 10. Top merchants by fraud count
-- --------------------------------------------

SELECT
    merchant,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(SUM(amount), 2) AS total_amount

FROM transactions

GROUP BY merchant

ORDER BY fraud_transactions DESC

LIMIT 10;


-- 11. Daily fraud activity
-- --------------------------------------------

SELECT
    DATE(transaction_date) AS transaction_day,

    COUNT(*) AS total_transactions,

    SUM(is_fraud) AS fraud_transactions,

    ROUND(
        100.0 * SUM(is_fraud) / COUNT(*),
        2
    ) AS fraud_rate

FROM transactions

GROUP BY transaction_day

ORDER BY transaction_day;


-- 12. Customer ranking by transaction amount
-- --------------------------------------------

WITH customer_transactions AS (

    SELECT
        c.customer_id,
        c.city,

        ROUND(SUM(t.amount), 2)
            AS total_amount

    FROM customers c

    JOIN accounts a
        ON c.customer_id = a.customer_id

    JOIN transactions t
        ON a.account_id = t.account_id

    GROUP BY
        c.customer_id,
        c.city
)

SELECT
    customer_id,
    city,
    total_amount,

    RANK() OVER (
        ORDER BY total_amount DESC
    ) AS customer_rank

FROM customer_transactions

ORDER BY customer_rank;


-- 13. Top 10 customers by fraud count
-- --------------------------------------------

WITH customer_fraud AS (

    SELECT
        c.customer_id,
        c.city,

        COUNT(t.transaction_id)
            AS transaction_count,

        SUM(t.is_fraud)
            AS fraud_count

    FROM customers c

    JOIN accounts a
        ON c.customer_id = a.customer_id

    JOIN transactions t
        ON a.account_id = t.account_id

    GROUP BY
        c.customer_id,
        c.city
)

SELECT
    customer_id,
    city,
    transaction_count,
    fraud_count,

    ROUND(
        100.0 * fraud_count
        / transaction_count,
        2
    ) AS fraud_rate

FROM customer_fraud

ORDER BY fraud_count DESC

LIMIT 10;