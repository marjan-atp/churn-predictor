import streamlit as st

st.set_page_config(page_title="Test", page_icon="🏦")
st.title("🏦 Test - App is Working!")
st.write("If you can see this, Streamlit is fine.")

try:
    import joblib
    model = joblib.load('best_churn_model.pkl')
    st.success("✅ Model loaded successfully!")
    st.write(type(model))
except Exception as e:
    st.error(f"❌ Model failed to load: {e}")
