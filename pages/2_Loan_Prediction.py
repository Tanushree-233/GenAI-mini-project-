
import streamlit as st

st.title("🎯 Loan Prediction")

income = st.slider("Income",10000,100000,50000)
credit = st.slider("Credit Score",300,850,700)
loan = st.slider("Loan Amount",10000,500000,200000)

if credit < 600:
    decision="Rejected"
elif credit < 700:
    decision="Under Review"
else:
    decision="Approved"

st.subheader(f"Loan Decision: {decision}")
