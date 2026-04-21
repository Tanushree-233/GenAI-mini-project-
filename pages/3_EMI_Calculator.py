import streamlit as st

st.title("💳 EMI Calculator")

loan = st.slider("Loan Amount",10000,500000,200000)
interest = st.slider("Interest Rate (%)",1,20,10)
tenure = st.slider("Loan Tenure (months)",6,120,36)

P = loan
r = interest/(12*100)
n = tenure

if r>0:
    emi=(P*r*(1+r)**n)/((1+r)**n-1)
else:
    emi=P/n

st.subheader(f"Monthly EMI: ₹{round(emi,2)}")
