import streamlit as st
import requests

st.title("Sentiment Analysis App (Transformer Model)")

text = st.text_area("Enter text for sentiment prediction:")

if st.button("Predict"):
    if not text.strip():
        st.warning("Please enter some text!")
    else:
        try:
            response = requests.post("http://backend:5000/predict", json={"text": text})
            result = response.json()
            st.success(f"Prediction: {result['label']} ({result['confidence']*100:.2f}%)")
            
            st.subheader("Explanation:")
            for word, score in result.get("explanation", []):
                st.write(f"**{word}** — Score: {score:.4f}")
        except Exception as e:
            st.error(f"Backend error: {e}")
