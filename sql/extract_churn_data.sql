-- Query to extract subscriber demographics, contract types, and billing history for churn modeling
WITH customer_tenure_cohorts AS (
    SELECT 
        customer_id,
        tenure_months,
        monthly_charges,
        total_charges,
        contract_type,
        payment_method,
        tech_support,
        churn,
        CASE 
            WHEN tenure_months <= 12 THEN '0-1 Year'
            WHEN tenure_months <= 36 THEN '1-3 Years'
            ELSE '3+ Years'
        END AS tenure_cohort
    FROM telecom_customers
)
SELECT 
    customer_id,
    tenure_months,
    tenure_cohort,
    monthly_charges,
    total_charges,
    contract_type,
    payment_method,
    tech_support,
    churn
FROM customer_tenure_cohorts
WHERE total_charges IS NOT NULL
ORDER BY tenure_months ASC;
