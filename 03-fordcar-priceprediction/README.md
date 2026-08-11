# Ford Car Price Prediction 🚗

## Overview

This project focuses on predicting the price of Ford cars using **Machine Learning regression techniques**.

The dataset was obtained from **Kaggle** and contains various features related to Ford vehicles, which were used to train a Linear Regression model.

## Objective

The objective of this project is to:

- Explore and understand the Ford car dataset
- Perform data preprocessing
- Encode categorical features
- Prepare the dataset for machine learning
- Train a Linear Regression model
- Evaluate the regression model using appropriate metrics
- Analyze how well the model predicts car prices

## Dataset

The dataset was obtained from **Kaggle** and contains information about Ford cars.

Some of the features include:

- Model
- Year
- Transmission
- Mileage
- Fuel Type
- Tax
- MPG
- Engine Size
- Price  
The target variable is:  
**Price**

## Data Preprocessing
The following preprocessing steps were performed:
  
 - Checked and handled missing values  
 - Separated features and target variable  
 - Encoded categorical variables using One-Hot Encoding  
 - Prepared the dataset for model training  
 - Split the data into training and testing sets  
   
## Machine Learning Model  
The model used for this project is:  
**Linear Regression**
Linear Regression was used to model the relationship between the car features and its price.
   
## Model Evaluation  
The model was evaluated using:  
 - **R² Score**
 - **Adjusted R² Score**
   
### Results

| Metric | Score |
|---|---:|
| R² Score | ~73% |
| Adjusted R² Score | ~73% |
the model achieved an R² score of approximately **73%**, meaning that the model explains around 73% of the variation in Ford car prices based on the features provided.
the Adjusted R² score was also approximately **73%**, indicating a similar level of explanatory power after accounting for the number of predictors in the model.
   
## Project Workflow
```text
Kaggle Dataset
      ↓
Data Exploration
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
One-Hot Encoding
      ↓
Train-Test Split
      ↓
Linear Regression
      ↓
Model Prediction
      ↓
Model Evaluation
      ↓
R² & Adjusted R²
```
## Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook

## Conclusion
A Linear Regression model was developed to predict Ford car prices using features such as model, year, mileage, transmission, fuel type, tax, MPG, and engine size.
The model achieved approximately 73% R² and Adjusted R², showing that the selected features provide a reasonable ability to explain variations in Ford car prices.
This project helped build an understanding of regression-based machine learning, categorical feature encoding, model evaluation, and interpreting R²-based performance metrics.