# House-Price-Prediction_System
Flask-based House Price Prediction web app that uses a trained Ridge Regression model to estimate house prices from number of beds, baths, size (sqft), and zip code. The UI is built with HTML/CSS and Jinja2 templates, and the backend loads a pre-trained model with pandas and scikit-learn to generate predictions.


# House Price Prediction System

A Flask-based web application that predicts house prices using a trained Ridge Regression model. Users can select the number of bedrooms, bathrooms, house size (in sqft), and zip code from dropdowns, and the app returns an estimated price in INR.

## Overview

This project demonstrates a complete machine learning workflow:

- Data pre-processing and model training done offline.
- The trained Ridge Regression model is saved as a `.pkl` file.
- A Flask backend loads the model and exposes a `/predict` endpoint.
- An HTML/Jinja2 frontend sends user inputs via `fetch` and displays the predicted price dynamically on the page.

The focus is on integrating an ML model into a production-style web interface.

## Features

- Clean web UI for entering property details.
- Flask API endpoint for inference.
- Uses `pandas` to construct input data for the model.
- Handles unseen categories in input by replacing them with the most frequent values from the training data.
- Modular structure so the model or dataset can be swapped easily.

## Project Structure

- `main.py` – Flask application, routing, and prediction logic.
- `templates/index.html` – Frontend form and JavaScript for sending requests and rendering the output.
- `final_datase.xls` – Processed dataset used during model development.
- `RidgeModel.pkl` – Serialized Ridge Regression model.
- `requirements.txt` – List of required Python packages.

## Getting Started

### 1. Clone the repository

git clone https://github.com/Venkat-Sai-Charan-Saragan/House-Price-Prediction_System.git
cd House-Price-Prediction_System


### 2. Create and activate a virtual environment (recommended)

python -m venv venv
venv\Scripts\activate # on Windows

source venv/bin/activate # on Linux/Mac


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the application

python main.py


Open the app in your browser:

http://127.0.0.1:5000/

Choose the property details and click **Predict Price** to see the model’s prediction.

## Technologies Used

- **Backend:** Python, Flask  
- **Machine Learning:** scikit-learn (Ridge Regression), pandas  
- **Frontend:** HTML, CSS, JavaScript, Jinja2 templates

## Possible Improvements

- Add model training notebook and scripts to the repo.
- Add form validation and better error handling on the frontend.
- Containerize the app with Docker for easier deployment.
- Deploy to a cloud platform (Render, Railway, Heroku alternative, etc.).


