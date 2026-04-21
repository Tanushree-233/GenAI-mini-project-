import streamlit as st
import matplotlib.pyplot as plt

st.title("💰 EMI Calculator")

# Inputs
loan_amount = st.slider("Loan Amount", 10000, 1000000, 200000)
interest_rate = st.slider("Interest Rate (%)", 1.0, 20.0, 10.0)
tenure = st.slider("Loan Tenure (months)", 6, 120, 12)

# EMI Formula
r = interest_rate / 12 / 100

emi = loan_amount * r * (1 + r) ** tenure / ((1 + r) ** tenure - 1)

st.subheader(f"Monthly EMI: ₹{round(emi,2)}")

# Payment details
total_payment = emi * tenure
total_interest = total_payment - loan_amount

st.subheader("Payment Breakdown")

data = [loan_amount, total_interest]
labels = ["Principal", "Interest"]

fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)
