import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

# Load the trained classifier
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"  

def predict_note_authentication(variance, skewness, curtosis, entropy):
    """
    Let's Authenticate the Banks Note 
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
    # Convert inputs to float
    variance = float(variance)
    skewness = float(skewness)
    curtosis = float(curtosis)
    entropy = float(entropy)
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return prediction

def main():
    st.title("Bank Authenticator")
    
    # Header
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Inputs
    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("Skewness", "Type Here")
    curtosis = st.text_input("Curtosis", "Type Here")
    entropy = st.text_input("Entropy", "Type Here")
    
    # Prediction
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.success(f"The output is {result}")  # backend remains 0/1
    
    # Sidebar to show meaning of 0 and 1
    st.sidebar.markdown("### Note Meaning")
    st.sidebar.markdown("0 → Genuine Note ✅")
    st.sidebar.markdown("1 → Fake Note ❌")
    
    # About button
    if st.button("About"):
        st.text("Lets rock India")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
