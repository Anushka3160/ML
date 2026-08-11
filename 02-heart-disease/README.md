# Heart Disease Prediction ❤️

## Overview

This project focuses on predicting the likelihood of heart disease using machine learning.

A **Logistic Regression** model was trained on heart disease data and then integrated into an interactive **Streamlit** application. The application allows users to enter health-related features and receive a model prediction.

## Objective

The objective of this project is to:

- Explore and preprocess heart disease data
- Prepare features for machine learning
- Train a classification model
- Scale the input features
- Save the trained model and preprocessing objects
- Build an interactive Streamlit application
- Use the trained model to generate predictions from user input

## Machine Learning Model

The classification model used in this project is:

**Logistic Regression**

The trained model and preprocessing components were saved using **Joblib** and loaded into the Streamlit application.

## Features Used

The application takes the following inputs:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

## Project Workflow

```text
Data
  ↓
Data Cleaning & Preprocessing
  ↓
Feature Encoding
  ↓
Feature Scaling
  ↓
Train-Test Split
  ↓
Logistic Regression
  ↓
Model Evaluation
  ↓
Save Model & Preprocessing Objects
  ↓
Streamlit Application
  ↓
User Input → Prediction
```
## Streamlit Application

The trained model was integrated into a Streamlit application.

The application allows users to enter the required health-related features and generates one of two model predictions:

⚠️ High Risk of Heart Disease
✅ Low Risk of Heart Disease

## Technologies Used

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Streamlit
Jupyter Notebook

## Project Structure

```text
heart-disease-prediction/
│
├── app.py
├── LogisticRegression_heart_model.pkl
├── heart_scaler.pkl
├── heart_columns.pkl
├── README.md
└── heart.ipynb
├── heart.csv
```

## How to Run the Application

1. Install the required libraries
```python
python -m pip install streamlit pandas scikit-learn joblib
```
2. Run the Streamlit application
```python
python -m streamlit run app.py
```

The application will open in your browser.

## Conclusion

This project demonstrates an end-to-end machine learning workflow, from preprocessing and model training to deploying the trained model as an interactive Streamlit application.

The project helped me understand how a trained machine learning model can be integrated into a user-facing application rather than being limited to a Jupyter Notebook.

Disclaimer: This application is developed for educational purposes only and is not intended to provide medical diagnosis or medical advice.