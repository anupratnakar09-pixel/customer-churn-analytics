import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Telecom Churn Predictor", layout="centered")

st.title("📊 Telecom Customer Churn Prediction")
st.write("Input subscriber details below to evaluate real-time churn risk probability.")

# Sidebar Controls
st.sidebar.header("Customer Profile")
tenure = st.sidebar.slider("Tenure (Months)", 1, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges ($)", 18.0, 120.0, 65.0)

contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
tech_support = st.sidebar.selectbox("Tech Support", ["No", "Yes"])
payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# Risk Scoring Logic
risk_score = 0.10
if contract == "Month-to-month": risk_score += 0.35
if tech_support == "No": risk_score += 0.25
if payment_method == "Electronic check": risk_score += 0.15
if tenure < 12: risk_score += 0.10

risk_percentage = min(risk_score, 0.95)

st.subheader("Risk Assessment Result")
if risk_percentage >= 0.50:
    st.error(f"⚠️ High Risk of Churn: {risk_percentage:.1%}")
    st.warning("Recommendation: Offer a 10% discount incentive for transitioning to an annual contract.")
else:
    st.success(f"✅ Low Risk Subscriber: {risk_percentage:.1%}")
    st.info("Recommendation: Maintain standard onboarding engagement.")
