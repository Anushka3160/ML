# Titanic Survival Prediction 🚢

## Overview

This project focuses on predicting whether a passenger survived the Titanic disaster using machine learning classification algorithms.

The Titanic dataset was loaded directly from the **Seaborn** library and used for data exploration, preprocessing, model training, and evaluation.

## Objective

The objective of this project is to train and compare multiple classification algorithms and identify the model that performs best at predicting passenger survival.

## Dataset

The Titanic dataset was loaded using Seaborn:

```python
import seaborn as sns
df = sns.load_dataset("titanic")
```

The dataset contains passenger information such as:
- Passenger class
- Sex
- Age
- Fare
- Number of siblings/spouses aboard
- Number of parents/children aboard
- Port of embarkation
- Survival status

## Classification Models

Five classification algorithms were trained and evaluated:
1. Logistic Regression  
2. K-Nearest Neighbors (KNN)  
3. Naive Bayes  
4. Decision Tree  
5. Support Vector Machine (SVM)

## Model Performance
| Model | Accuracy |
|---|---|
| Logistic Regression | 80% |
| K-Nearest Neighbors (KNN) | 78% |
| Naive Bayes | 77% |
| Decision Tree | 76% |
| Support Vector Machine (SVM) | 82% |

## Best Performing Model
The Support Vector Machine (SVM) achieved the highest test accuracy of **82%**, making it the best-performing model among the five classification algorithms tested.

## Performance Ranking 
🥇 SVM — 82%
🥈 Logistic Regression — 80%
🥉 KNN — 78%
Naive Bayes — 77%
Decision Tree — 76%

## Project Workflow
a. Load the Titanic dataset using Seaborn   
b. Explore and understand the dataset   
c. Handle missing values   
d. Perform data preprocessing   
e. Encode categorical features   
f. Split the data into training and testing sets   
g. Train five classification models   
h. Evaluate model performance   
i. Compare model results   j. Select the best-performing model.

## Technologies Used
defaults:
python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook.

## Conclusion
the support vector machine (SVM) achieved the highest test accuracy of **82%**, followed by logistic regression with **80%**.
this project demonstrates the importance of comparing multiple machine learning algorithms to identify the most suitable model for a classification problem.