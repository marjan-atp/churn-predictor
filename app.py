import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Churn Predictor", page_icon="🏦", layout="centered")

model = joblib.load('best_model.pkl')
scaler = joblib.load('my_scaler.pkl')

st.title("🏦 Bank Customer Churn Predictor")
st.write("Enter the customer's details below to predict if they will leave the bank.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal Details")
    Geography = st.selectbox("Geography (Country)", ["France", "Germany", "Spain"])
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.slider("Age", min_value=18, max_value=100, value=35)
    Tenure = st.slider("Tenure (Years with Bank)", min_value=0, max_value=10, value=5)
    EstimatedSalary = st.number_input("Estimated Salary ($)", min_value=0.0, value=60000.0, step=1000.0)

with col2:
    st.subheader("Account Details")
    CreditScore = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    Balance = st.number_input("Account Balance ($)", min_value=0.0, value=50000.0, step=1000.0)
    NumOfProducts = st.selectbox("Number of Products", [1, 2, 3, 4])
    HasCrCard = st.selectbox("Has Credit Card?", ["Yes", "No"])
    IsActiveMember = st.selectbox("Is Active Member?", ["Yes", "No"])

st.markdown("---")

has_crcard_encoded = 1 if HasCrCard == "Yes" else 0
is_active_encoded = 1 if IsActiveMember == "Yes" else 0
gender_encoded = 1 if Gender == "Male" else 0
geo_dict = {"France": 0, "Germany": 1, "Spain": 2}
geography_encoded = geo_dict[Geography]

if st.button("Predict Churn Risk", type="primary", use_container_width=True):
    input_data = pd.DataFrame({
        'CreditScore': [CreditScore],
        'Geography': [geography_encoded],
        'Gender': [gender_encoded],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [NumOfProducts],
        'HasCrCard': [has_crcard_encoded],
        'IsActiveMember': [is_active_encoded],
        'EstimatedSalary': [EstimatedSalary]
    })

    scaled_input = scaler.transform(input_data)

    probability = model.predict_proba(Scaled_input)[0][1] * 100

    # Adjusted threshold to account for SMOTE overcorrection
    threshold = 0.55  

    st.markdown("### Prediction Results:")
    if probability / 100 >= threshold:
        st.error("⚠️ **High Risk of Churn!**")
        st.write(f"The model predicts a **{probability:.1f}%** probability of churn.")
    else:
        st.success("✅ **Safe: Customer is likely to stay.**")
        st.write(f"The model predicts only a **{probability:.1f}%** probability of churn.")
