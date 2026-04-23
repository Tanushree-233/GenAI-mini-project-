import streamlit as st
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
text-align:center;
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

# ---------- DASHBOARD IMAGE ----------

st.markdown("### Financial Analytics Overview")

st.image(
"https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80",
use_container_width=True
)

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

# ---------- CHAT MEMORY ----------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- HELPER FUNCTIONS ----------

def extract_values(text):
    numbers = list(map(int, re.findall(r'\d+', text)))
    if len(numbers) >= 2:
        return numbers[0], numbers[1], 200000
    return 50000, 700, 200000


def generate_answer(income, credit, loan, user_input):

    q = user_input.lower()

    # -------- DETECT NUMERIC INPUT (PREDICTION MODE) --------
    numbers = re.findall(r'\d+', user_input)

    if len(numbers) >= 2:

        if credit < 500:
            decision = "Rejected"
        elif credit > 700:
            decision = "Approved"
        else:
            decision = "Likely Approved"

        risk_score = max(10, int(100 - (credit / 8)))

        return f"{decision} — Risk Score: {risk_score}/100"

    # -------- EXPLANATION MODE --------

    if "credit score" in q:
        return "A credit score is a number that represents your creditworthiness. Higher scores increase loan approval chances."

    if "risk" in q:
        return "Loan risk indicates the probability of default. Higher credit score means lower risk."

    if "important" in q:
        return "Credit score reflects repayment behaviour and is very important in loan approval."

    if "loan approval" in q:
        return "Loan approval depends on credit score, income, and loan amount."

    return "Please provide income and credit score to predict loan approval."

# ---------- CHATBOT ----------

st.subheader("💬 FinCred AI Assistant")

user_input = st.chat_input("Ask about credit score, loan risk, or approval...")

if user_input:

    income, credit, loan = extract_values(user_input)

    response = generate_answer(income, credit, loan, user_input)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("assistant", response))

for role, msg in st.session_state.messages:

    with st.chat_message(role):
        st.markdown(msg)

st.markdown("---")

st.caption("🚀 FinCred AI | Smart Loan Decision System")
