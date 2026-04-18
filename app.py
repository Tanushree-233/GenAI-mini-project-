
import streamlit as st
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import PyPDF2

# Load fine-tuned model
model_path = "Tanushree23/pdf-qa-finetuned-model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)

qa_pipeline = pipeline(
    "question-answering",
    model=model,
    tokenizer=tokenizer
)

st.title("PDF Question Answering System")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

context = ""

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            context += text

    st.success("PDF loaded successfully!")

    question = st.text_input("Ask a question from the PDF")

    if st.button("Get Answer"):

        # Split context into chunks
        chunks = [context[i:i+500] for i in range(0, len(context), 500)]

        best_answer = ""
        best_score = 0

        for chunk in chunks:
            result = qa_pipeline(question=question, context=chunk)

            if result["score"] > best_score:
                best_score = result["score"]
                best_answer = result["answer"]

        st.success(best_answer)
