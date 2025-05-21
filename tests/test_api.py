#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 17:32:01 2025

@author: jalalfarj
"""

import requests
import requests
import time

BASE_URL = "http://fastapi:8000"

# Retry logic to wait for FastAPI to be ready
def wait_for_api(timeout=15):
    for _ in range(timeout):
        try:
            response = requests.get(f"{BASE_URL}/docs")
            if response.status_code == 200:
                print("✅ FastAPI is up")
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    raise RuntimeError("❌ FastAPI not ready after waiting")

def test_predict_route_exists():
    wait_for_api()
    response = requests.post(f"{BASE_URL}/predict", json={
        "age": 57, "sex": 1, "cp": 0, "trestbps": 140, "chol": 260,
        "fbs": 0, "restecg": 1, "thalach": 120, "exang": 0,
        "oldpeak": 1.2, "slope": 1, "ca": 0, "thal": 2
    })
    assert response.status_code == 200

def test_response_has_prediction():
    wait_for_api()
    response = requests.post(f"{BASE_URL}/predict", json={
        "age": 57, "sex": 1, "cp": 0, "trestbps": 140, "chol": 260,
        "fbs": 0, "restecg": 1, "thalach": 120, "exang": 0,
        "oldpeak": 1.2, "slope": 1, "ca": 0, "thal": 2
    })
    result = response.json()
    assert "prediction" in result
    assert result["prediction"] in [0, 1]
