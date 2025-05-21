#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 15:04:06 2025

@author: jalalfaraj
"""

import streamlit as st
import joblib
import numpy as np
import os

st.title("🫀 Heart Disease Predictor")

# Load model
MODEL_PATH = "models/heart_model.pkl"
if not os.path.exists(MODEL_PATH):
    st.error("Model file not found. Please make sure heart_model.pkl is in the models/ folder.")
else:
    model = joblib.load(MODEL_PATH)

    # Input form
    age = st.number_input("Age", min_value=0, max_value=120, value=57)
    sex = st.selectbox("Sex", [0, 1])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", value=140)
    chol = st.number_input("Serum Cholesterol (mg/dl)", value=260)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", value=120)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression", value=1.2)
    slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
    ca = st.number_input("Number of Major Vessels (0–3)", min_value=0, max_value=3, value=0)
    thal = st.selectbox("Thalassemia", [1, 2, 3])

    input_data = np.array([[
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach, exang,
        oldpeak, slope, ca, thal
    ]])

    if st.button("Predict"):
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("⚠️ High risk of heart disease.")
        else:
            st.success("✅ No heart disease detected.")
