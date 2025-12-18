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
