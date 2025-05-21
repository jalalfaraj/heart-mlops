#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:54:52 2025

@author: jalalfaraj
"""

# Project: MLOps Heart Disease Prediction Pipeline

# Goal: Build a deployable, trackable, and reproducible ML pipeline to predict heart disease using basic patient data.
# Tools: scikit-learn, FastAPI, MLflow, Docker, GitHub Actions (CI), optional: Streamlit/Gradio

# Step 1: Load data and train model with MLflow (src/train.py)
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset (UCI Heart Disease dataset)
import pandas as pd

column_names = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
    'ca', 'thal', 'target'
]

data = pd.read_csv('../data/processed.cleveland.data', names=column_names)


data.replace('?', pd.NA, inplace=True)
data.dropna(inplace=True)

data = data.astype({
    'age': float,
    'sex': int,
    'cp': int,
    'trestbps': float,
    'chol': float,
    'fbs': int,
    'restecg': int,
    'thalach': float,
    'exang': int,
    'oldpeak': float,
    'slope': int,
    'ca': float,
    'thal': float,
    'target': int
})

X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Enable auto-logging to MLflow
mlflow.set_experiment("heart_disease_classifier")

with mlflow.start_run():
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(clf, "model")

    # Save model to local file
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "../models/heart_model.pkl")

print(f"Model trained. Accuracy: {acc:.4f}")