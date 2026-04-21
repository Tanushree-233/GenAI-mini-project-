import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📂 Bulk Loan Prediction")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.dataframe(df)

    def predict(row):

        credit = row["CreditScore"]

        if credit < 600:
            return "Rejected"
        elif credit >= 700:
            return "Approved"
        else:
            return "Under Review"

    df["Decision"] = df.apply(predict, axis=1)

    st.dataframe(df)

    chart = df["Decision"].value_counts().reset_index()
    chart.columns=["Decision","Count"]

    fig=px.pie(chart,values="Count",names="Decision")

    st.plotly_chart(fig)
