import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📂 Bulk Loan Prediction")

uploaded_file = st.file_uploader("Upload Customer Data CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")
    st.dataframe(df)

    # Let user choose credit score column
    credit_column = st.selectbox(
        "Select the Credit Score Column",
        df.columns
    )

    # Prediction logic
    def predict(row):

        credit = row[credit_column]

        if credit < 600:
            return "Rejected"
        elif credit >= 700:
            return "Approved"
        else:
            return "Under Review"

    # Apply prediction
    df["LoanDecision"] = df.apply(predict, axis=1)

    st.subheader("Prediction Results")
    st.dataframe(df)

    # Decision distribution chart
    chart = df["LoanDecision"].value_counts().reset_index()
    chart.columns = ["Decision", "Count"]

    fig = px.pie(
        chart,
        values="Count",
        names="Decision",
        title="Loan Decision Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
