import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/predict"
# Streamlit UI

st.title(" Iris Flower Classifier")
st.markdown("Enter flower dimensions to predict its species.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    # Data payload
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:
        # Make request to FastAPI backend
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()

        if response.status_code == 200:
            st.success(f"🌟 Predicted Species: **{result['predicted_class'].title()}**")
        else:
            st.error(f"Error: {result['error']}")
    except Exception as e:
        st.error(f" Could not connect to FastAPI server.\n\nError: {str(e)}")
