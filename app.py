# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KPOdbm8UYpRsdAlxASK1J1k4_oN_6GV1
"""

import nltk
from nltk.tokenize import word_tokenize
import string
import streamlit as st

# Download NLTK resources
nltk.download('punkt')

# Preprocessing function
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text
    word_tokens = word_tokenize(text)

    # Remove punctuation and stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_words = [word for word in word_tokens if word not in stop_words and word not in string.punctuation]

    return ' '.join(filtered_words)

# Streamlit interface
st.title("Sentiment Analysis on IMDb Reviews")

# User input for review text
user_input = st.text_area("Enter your movie review:")

# Preprocess input text
if user_input:
    preprocessed_input = preprocess_text(user_input)
    st.write("Preprocessed Text:", preprocessed_input)

    # Load model (make sure the model file is correct)
    # model = joblib.load('imdb_model.pkl')  # Load your trained model here

    # Predict sentiment (use your model for prediction here)
    # sentiment = model.predict([preprocessed_input])

    # Display the prediction result
    # st.write("Sentiment:", sentiment)

# Note: Make sure your model file is in the same directory or provide the correct path.
