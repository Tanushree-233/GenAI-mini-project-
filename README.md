# FinCred AI – Smart Loan Decision System

## Overview

FinCred AI is an intelligent loan decision support dashboard built using Python and Streamlit. The system analyzes financial parameters such as income, credit score, and loan amount to estimate loan approval probability and evaluate loan risk.

The application integrates AI-assisted explanations, financial analytics, and interactive visualizations to simulate a modern financial decision support system used in banking and fintech environments.

The dashboard also supports bulk loan analysis through CSV uploads, allowing predictions for multiple customers simultaneously.

---
## Live Demo

Streamlit App: https://oeuzhpj3xgjriz7cyitljf.streamlit.app/
## Features

### Loan Decision Dashboard
The dashboard evaluates financial inputs and estimates loan approval probability. It includes:

- Loan approval probability calculation
- Risk score visualization using a gauge chart
- Risk category classification (Low, Medium, High)
- Loan decision indicator

### AI Loan Assistant
The system includes a chat assistant powered by a pre-trained language model (DistilGPT-2). Users can ask questions related to loan risk and credit score importance.

### Explainable AI
The dashboard provides explanations for loan approval decisions based on credit score and financial risk indicators.

### EMI Calculator
The system calculates estimated monthly loan payments based on:

- Loan amount
- Interest rate
- Loan tenure

### Financial Visualization
Interactive charts visualize financial parameters such as income, credit score, and loan amount.

### PDF Report Generation
Users can generate and download a loan analysis report containing:

- Financial inputs
- Approval probability
- Risk score
- Decision outcome

### Bulk Loan Prediction
Users can upload a CSV dataset to analyze multiple loan applications simultaneously. The system automatically predicts loan approval outcomes and visualizes the distribution of decisions.

---

## Technology Stack

**Programming Language**
Python

**Frontend Framework**
Streamlit

**AI Model**
Hugging Face Transformers (DistilGPT-2)

**Data Processing**
Pandas

**Visualization**
Plotly

**Report Generation**
ReportLab

---

## Project Structure

```
FinCred-AI
│
├── app.py
├── requirements.txt
├── README.md
└── pages 

```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/FinCred-AI.git
```

Move into the project directory:

```
cd FinCred-AI
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit application:

```
streamlit run app.py
```

---

## CSV Dataset Format for Bulk Prediction

The CSV file should include at least the following column:

```
CreditScore
```

Example dataset format:

```
Income,CreditScore,LoanAmount
50000,720,200000
40000,650,150000
30000,480,100000
70000,780,250000
```

The system will automatically generate loan decision predictions for each record.

---

## Applications

- Loan risk assessment for financial institutions  
- Creditworthiness evaluation for loan applicants  
- Interactive financial analytics dashboards  
- AI-assisted loan decision systems  

---

## Future Improvements

- Integration of trained machine learning models
- Customer risk heatmap visualization
- Loan recommendation system
- Database integration for customer records
- Advanced credit scoring algorithms

---

## License

This project is developed for academic and educational purposes
