# Sentiment-Analysis-on-IMDB-reviews
# IMDB Sentiment Analysis

This project is a **Sentiment Analysis** application for movie reviews using a machine learning model trained on the IMDB dataset. The goal of this project is to predict whether a movie review is **positive** or **negative** based on the text provided by the user. The model has been trained and deployed using Streamlit for interactive web-based deployment.

## Features
- **User Input**: Users can input movie reviews into a text box.
- **Sentiment Prediction**: The model predicts whether the review is **positive** or **negative**.
- **Model Integration**: The application uses a pre-trained model (saved as `.pkl`) to make predictions.
- **Preprocessing**: Text preprocessing techniques are applied to ensure high-quality input data for the model.

## Technologies Used
- **Python**: Programming language used to develop the application.
- **Streamlit**: Framework for building and deploying the app.
- **NLTK**: Natural Language Toolkit for text preprocessing (tokenization, stopword removal, etc.).
- **Scikit-learn**: For machine learning model building and evaluation.
- **Joblib**: Used to save and load the trained model.

## Requirements

To run this application, you need to have the following Python libraries installed:
- `streamlit`
- `nltk`
- `scikit-learn`
- `joblib`

You can install the required libraries using pip:

```bash
pip install streamlit nltk scikit-learn joblib
