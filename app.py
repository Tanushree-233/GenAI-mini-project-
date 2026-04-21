import streamlit as st
import re

st.set_page_config(page_title="FinCred AI", layout="wide")

# ----------- THEME -----------

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}
.card{
background: rgba(255,255,255,0.08);
padding:20px;
border-radius:16px;
backdrop-filter: blur(10px);
}
h1,h2,h3,h4,h5,h6,p,span,label{
color:white !important;
}
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ----------- TITLE -----------

st.markdown("<h1 style='text-align:center;'>🏦 FinCred AI</h1>", unsafe_allow_html=True)
st.caption("Smart Loan Decision System")

st.markdown("""
FinCred AI is an intelligent **loan decision support system** built using
Python and Streamlit.

The system analyzes financial parameters such as:

• Income  
• Credit Score  
• Loan Amount  

and provides **loan approval probability and risk analysis**.

Use the **sidebar pages** to explore:

• Dashboard  
• Loan Prediction  
• EMI Calculator  
• Bulk Prediction
""")

st.markdown("---")

# ----------- CHAT MEMORY -----------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------- HELPER FUNCTIONS -----------

def extract_values(text):
    numbers = list(map(int,re.findall(r'\d+',text)))
    if len(numbers)>=2:
        return numbers[0],numbers[1],200000
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


# ----------- CHATBOT -----------

st.subheader("💬 FinCred AI Assistant")

user_input = st.chat_input("Ask about loans, credit score, or risk...")

if user_input:

    income,credit,loan = extract_values(user_input)

    res = generate_answer(income,credit,loan,user_input)

    st.session_state.messages.append(("user",user_input))
    st.session_state.messages.append(("assistant",res))


for role,msg in st.session_state.messages:

    with st.chat_message(role):

        st.markdown(msg)

st.markdown("---")

st.caption("🚀 FinCred AI | Smart Loan Decision System")
