import os
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

# Deployment-safe pickle loading
try:
    # Local or normal execution
    pickle_path = os.path.join(os.path.dirname(__file__), "classifier.pkl")
except NameError:
    # Streamlit Cloud (__file__ not defined)
    pickle_path = "classifier.pkl"

if not os.path.exists(pickle_path):
    st.error(f"Pickle file not found at {pickle_path}")
else:
    with open(pickle_path, "rb") as pickle_in:
        classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance, skewness, curtosis, entropy):
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")

    result = ""
    if st.button("Predict"):
        try:
            # Convert inputs to float before prediction
            var = float(variance)
            skew = float(skewness)
            curt = float(curtosis)
            ent = float(entropy)
            result = predict_note_authentication(var, skew, curt, ent)
        except ValueError:
            result = "Please enter valid numbers"

    st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Love from India")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
