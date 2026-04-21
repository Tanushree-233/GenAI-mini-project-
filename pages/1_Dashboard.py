
import streamlit as st
import plotly.graph_objects as go

st.title("📊 Loan Risk Dashboard")

credit = st.slider("Credit Score",300,850,700)

risk_score = max(10,100-(credit/8))

fig = go.Figure(go.Indicator(
mode="gauge+number",
value=risk_score,
title={"text":"Risk Score"},
gauge={
"axis":{"range":[0,100]},
"steps":[
{"range":[0,30],"color":"green"},
{"range":[30,60],"color":"yellow"},
{"range":[60,100],"color":"red"}
]
}
))

st.plotly_chart(fig)
