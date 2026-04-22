import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.title("🎯 Loan Prediction")

# ---------- INPUT SLIDERS ----------

income = st.slider("Income", 10000, 100000, 50000)
credit = st.slider("Credit Score", 300, 850, 700)
loan = st.slider("Loan Amount", 10000, 500000, 200000)

st.markdown("---")

# ---------- LOAN DECISION ----------

if credit < 600:
    decision = "Rejected"
elif credit < 700:
    decision = "Under Review"
else:
    decision = "Approved"

st.subheader(f"Loan Decision: {decision}")

st.markdown("---")

# ---------- RISK SCORE ----------

risk_score = max(10, int(100 - (credit / 8)))

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_score,
    title={"text": "Risk Score"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "white"},
        "steps": [
            {"range": [0, 30], "color": "green"},
            {"range": [30, 60], "color": "yellow"},
            {"range": [60, 100], "color": "red"}
        ],
    }
))

st.plotly_chart(fig, use_container_width=True)

# ---------- RISK LEVEL ----------

if risk_score < 30:
    st.success("Low Risk")
elif risk_score < 60:
    st.warning("Medium Risk")
else:
    st.error("High Risk")

st.markdown("---")

# ---------- APPROVAL PROBABILITY ----------

if credit > 750:
    approval = 95
elif credit > 700:
    approval = 85
elif credit > 650:
    approval = 70
else:
    approval = 40

st.markdown(f"### Approval Probability: **{approval}%**")

st.markdown("---")

# ---------- AI EXPLANATION ----------

st.markdown("### AI Explanation")

if credit > 700:
    st.success("High credit score indicates reliable repayment behaviour.")
elif credit > 600:
    st.warning("Moderate credit score indicates medium loan risk.")
else:
    st.error("Low credit score increases default risk.")

st.markdown("---")

# ---------- FINANCIAL COMPARISON CHART ----------

data = {
    "Category": ["Income", "Loan Amount"],
    "Amount": [income, loan]
}

fig2 = px.bar(
    data,
    x="Category",
    y="Amount",
    title="Financial Comparison"
)

st.plotly_chart(fig2, use_container_width=True)
