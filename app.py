import streamlit as st
import re

st.set_page_config(page_title="FinCred AI", layout="wide")

# ------------------ TITLE ------------------

st.title("🏦 FinCred AI – Smart Loan Decision System")

st.write("""
FinCred AI is an intelligent financial decision dashboard that evaluates
loan applications using parameters like **income, credit score, and loan amount**.

The system provides:

• Loan approval probability  
• Risk score analysis  
• EMI calculation  
• Bulk dataset prediction  
• AI powered loan assistant
""")

st.image(
"https://images.unsplash.com/photo-1551288049-bebda4e38f71",
use_container_width=True
)

st.markdown("---")

# ------------------ CHATBOT ------------------

st.subheader("💬 AI Loan Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_answer(user_input):

    q = user_input.lower()

    if "credit score" in q:
        return "A credit score above 700 significantly increases loan approval chances."

    if "loan risk" in q:
        return "Loan risk depends mainly on credit score and income stability."

    if "important" in q:
        return "Credit score and repayment history are the most important factors."

    return "I can help explain loan approval factors like credit score, income, and risk."

user_input = st.chat_input("Ask about loans, credit score, or risk...")

if user_input:

    response = generate_answer(user_input)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("assistant", response))

for role, message in st.session_state.messages:

    with st.chat_message(role):

        st.markdown(message)
