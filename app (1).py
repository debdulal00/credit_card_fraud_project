import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("fraud_model.pkl")

st.set_page_config(page_title="💳 Credit Card Fraud Detection", layout="wide")

st.title("💳 Credit Card Fraud Detection App")
st.write("Predict whether a transaction is **Fraudulent (1)** or **Normal (0)** using your trained model.")

# Define input features
features = [
    'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
    'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21',
    'V22','V23','V24','V25','V26','V27','V28','Amount'
]

input_data = {}
st.sidebar.header("Enter Transaction Features")
for f in features:
    input_data[f] = st.sidebar.number_input(f, value=0.0, format="%.5f")

input_df = pd.DataFrame([input_data])
st.write("### Entered Transaction Data")
st.dataframe(input_df)

if st.button("🔍 Predict Fraud"):
    prediction = model.predict(input_df)[0]
    result = "❌ Fraudulent Transaction" if prediction == 1 else "✅ Normal Transaction"
    st.subheader(f"Prediction Result: **{result}**")

