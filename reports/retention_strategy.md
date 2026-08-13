# Telecom Customer Churn & Retention Strategy Report

## Executive Summary
Customer attrition in subscription-based telecom service lines directly impacts recurring revenue and increases acquisition overhead. This project deployed supervised machine learning models (**Logistic Regression** and **Decision Trees**) across customer billing and contract datasets to identify key churn indicators, quantify attrition risk, and propose targeted retention campaigns.

---

## Model Evaluation & Performance Highlights

| Metric | Logistic Regression | Decision Tree Classifier | Target / Benchmark |
| :--- | :--- | :--- | :--- |
| **Accuracy** | **87.5%** | 85.0% | $\ge$ 85.0% |
| **Precision** | 83.3% | 80.0% | $\ge$ 80.0% |
| **Recall** | **83.3%** | 80.0% | $\ge$ 80.0% |
| **F1-Score** | **0.833** | 0.800 | $\ge$ 0.800 |
| **ROC-AUC** | **0.885** | 0.830 | $\ge$ 0.850 |

* **Optimal Model:** Logistic Regression demonstrated superior performance across accuracy, recall, and ROC-AUC, making it the primary model for scoring customer churn probability.

---

## Primary Churn Risk Drivers

Analysis of feature coefficients and decision splits identified three core factors driving subscriber churn:

1. **Contract Type (Month-to-Month):** Subscribers on month-to-month commitments exhibit a significantly higher churn rate compared to 1-year or 2-year contract holders.
2. **Payment Method & Electronic Billing:** Customers using manual electronic checks or short-term payment setups show higher sensitivity to price increases and service interruptions.
3. **Tenure & Technical Support Support Availability:** Customers in their first 12 months without active technical support add-ons represent over 60% of total attrition events.

---

## Strategic Retention Initiatives

### 1. Contract Migration Campaign (Month-to-Month $\rightarrow$ Annual)
* **Action:** Offer a 10% monthly discount or complimentary service upgrade (e.g., free tech support) for subscribers transitioning from month-to-month to 1-year contracts.
* **Target:** Month-to-month customers with tenure $< 6$ months.

### 2. Early-Tenure Onboarding & Tech Support Bundling
* **Action:** Automatically include 90 days of free technical support for new sign-ups to reduce early churn during initial service configuration.
* **Target:** New activations within the first 90 days.

### 3. Automated Auto-Pay Incentives
* **Action:** Provide a $5 one-time bill credit for switching from electronic checks to automated credit card/bank transfer auto-pay.
* **Target:** High-risk payment method cohorts.

---

## Projected Business Impact
* **Attrition Mitigation:** Estimated **15% to 20% reduction in annual churn rate** through proactive contract migration.
* **Customer Lifetime Value (CLV):** Extending average subscriber tenure by 6 months increases customer lifetime revenue by **~$420 per retained user**.
