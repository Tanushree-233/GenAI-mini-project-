import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import re

st.set_page_config(page_title="FinCred AI", layout="wide")

# ---------- THEME ----------
st.markdown("""
<style>
.stApp{
  background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.card{
  background: rgba(255,255,255,0.08);
  padding:20px;
  border-radius:16px;
  backdrop-filter: blur(8px);
}

.banner{
  background: linear-gradient(135deg,#0b1320,#0f1f36);
  padding:30px;
  border-radius:18px;
  border:1px solid rgba(255,255,255,0.1);
}

h1,h2,h3,h4,p{
  color:white !important;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 style='text-align:center;'>🏦 FinCred AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Smart Loan Decision System</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------- DASHBOARD BANNER ----------
st.markdown('<div class="banner">', unsafe_allow_html=True)

b1, b2 = st.columns([1.4,1])

with b1:
    st.markdown("### Financial Analytics Overview")

    x = np.arange(10)
    y = np.cumsum(np.random.randn(10)) + 10

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", line=dict(color="#38bdf8", width=3)))
    fig.update_layout(
        height=180,
        margin=dict(l=0,r=0,t=0,b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=False, visible=False)
    )

    st.plotly_chart(fig, use_container_width=True)

    bar = px.bar(
        x=["Jan","Feb","Mar","Apr","May","Jun"],
        y=[5,7,9,8,10,11]
    )

    bar.update_layout(
        height=180,
        margin=dict(l=0,r=0,t=0,b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(bar, use_container_width=True)

with b2:
    st.markdown("""
    <div class="card">
    <h4>Revenue</h4>
    <h2>$120K</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>Expenses</h4>
    <h2>$80K</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Financial Dashboards That Scale")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------- KPI CARDS ----------
c1,c2,c3 = st.columns(3)

c1.markdown("""
<div class="card">
<h3>Loans Processed</h3>
<h2>120K</h2>
</div>
""", unsafe_allow_html=True)

c2.markdown("""
<div class="card">
<h3>Approved Loans</h3>
<h2>80K</h2>
</div>
""", unsafe_allow_html=True)

c3.markdown("""
<div class="card">
<h3>Approval Rate</h3>
<h2>66%</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- CHATBOT ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

def extract_values(text):
    numbers = list(map(int, re.findall(r'\d+', text)))
    if len(numbers) >= 2:
        return numbers[0], numbers[1], 200000
    return 50000,700,200000

def generate_answer(income,credit,loan,user_input):

    q=user_input.lower()

    if "important" in q:
        return "Credit score reflects repayment behaviour."

    if "risk" in q:
        return "Higher credit score means lower loan risk."

    if credit<500:
        decision="Rejected"
    elif credit>700:
        decision="Approved"
    else:
        decision="Likely Approved"

    risk_score=100-(credit//10)

    return f"{decision} — Risk Score: {risk_score}/100"

st.subheader("💬 FinCred AI Assistant")

user_input = st.chat_input("Ask about credit score, loan risk, or approval...")

if user_input:

    income,credit,loan = extract_values(user_input)

    response = generate_answer(income,credit,loan,user_input)

    st.session_state.messages.append(("user",user_input))
    st.session_state.messages.append(("assistant",response))

for role,msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)

st.markdown("---")
st.caption("🚀 FinCred AI | Smart Loan Decision System")
