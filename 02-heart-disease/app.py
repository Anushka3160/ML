import streamlit as st
import pandas as pd
import joblib

model = joblib.load("LogisticRegression_heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns=joblib.load("heart_columns.pkl")


st.title("Heart Stroke Prediction By Anushka❤️")
st.markdown("This app predicts the likelihood of heart stroke based on user input features. Please fill in the required information below and click 'Predict' to see the results.")
age=st.slider("Age",18,100,40)
se=st.selectbox("SEX",["Male","Female"])
chest_pain=st.selectbox("Chest Pain Type",["ATA","NAP","ASY","TA"])
resting_bp=st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol=st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
fasting_bs=st.selectbox("Fasting Blood Sugar > 120 mg/dl",["0","1"])
resting_ecg=st.selectbox("Resting ECG", ["Normal","ST","LVH"])
max_hr=st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina=st.selectbox("Exercise Induced Angina",["Y","N"])
oldpeak=st.slider("Oldpeak(ST Depression)", 0.0, 6.0, 1.0)
st_slope=st.selectbox("ST Slope", ["Up","Flat","Down"])

if st.button("Predict"):
    raw_input ={
        "Age": age,
        "Sex_"+ se: 1,
        "ChestPainType_"+ chest_pain: 1,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG_"+ resting_ecg: 1,
        "MaxHR": max_hr,
        "ExerciseAngina_"+ exercise_angina: 1,
        "Oldpeak": oldpeak,
        "ST_Slope_"+ st_slope: 1
    }
    imput_df=pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in imput_df.columns:
            imput_df[col] = 0
    input_df = imput_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")