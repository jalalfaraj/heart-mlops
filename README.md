# 🫀 Heart Disease MLOps Pipeline

![CI](https://github.com/jalalfaraj/heart-mlops/actions/workflows/mlops-ci.yml/badge.svg)

This project predicts heart disease using a production-grade MLOps stack. It includes model training, API deployment, interactive UI, and experiment tracking — all containerized and CI-enabled.

🌐 **Live Demo:** [View App on Streamlit](https://heart-mlops-fn7f9c7m9xwbrfho5znbw4.streamlit.app)

---

## 🚀 Features

- ✅ **Machine Learning**: RandomForestClassifier trained on the UCI Heart Disease dataset
- ⚡ **FastAPI**: Lightweight backend for serving predictions
- 🧪 **Test Suite**: Pytest integration to verify API predictions and outputs
- 💻 **Streamlit**: Simple UI for users to interact with the model
- 📈 **MLflow**: Track experiments, model performance, and parameters
- 🐳 **Docker Compose**: Orchestrate backend, frontend, and MLflow together
- 🔁 **GitHub Actions CI**: Automatically trains model + runs tests on every push

---

## 📁 Folder Structure

```
heart-mlops/
├── app/                  # FastAPI API
├── data/                 # Raw or downloaded datasets
├── models/               # Saved model artifacts (.pkl)
├── src/                  # Model training logic + MLflow tracking
├── tests/                # API tests with pytest
├── streamlit_app.py      # Frontend UI
├── Dockerfile            # FastAPI service
├── Dockerfile.streamlit  # Streamlit UI service
├── Dockerfile.mlflow     # MLflow tracking UI
├── docker-compose.yml    # Compose for all services
└── README.md             # This file
```

---

## ⚙️ How to Run Locally

> You'll need Docker and Docker Compose installed.

### Step 1: Clone the repo

```bash
git clone https://github.com/jalalfaraj/heart-mlops.git
cd heart-mlops
```

### Step 2: Run all services

```bash
docker-compose up --build
```

### Step 3: Open your browser:

- 🔌 **FastAPI (API)** → [http://localhost:8081/docs](http://localhost:8081/docs)
- 🖥 **Streamlit (UI)** → [http://localhost:8501](http://localhost:8501)
- 📊 **MLflow (Experiments)** → [http://localhost:5000](http://localhost:5000)

---

## 🧪 Run the Test Suite

```bash
docker-compose up --build tests
```

Tests include:
- `/predict` endpoint is live
- Prediction result is returned and valid

---

## 🔬 MLflow Tracking

You can view:
- Accuracy metrics
- Model versions
- Parameters

👉 `http://localhost:5000`

All runs are tracked under the experiment: `heart_disease_classifier`

---

## 🛠 Tech Stack

- Python, scikit-learn
- FastAPI + Uvicorn
- Streamlit
- MLflow
- Docker + Docker Compose
- GitHub Actions
- Pytest

---

## 📌 Future Improvements

- [ ] Add model tuning (GridSearchCV)
- [ ] Add input validation
- [ ] Deploy via Render / EC2
- [ ] Connect to a database for logging

---

## 🤝 Contributing

Feel free to fork, open issues, or suggest improvements!

---

## 🧠 Author

**Jalal Faraj**  
📫 [LinkedIn](https://www.linkedin.com/in/jalalfaraj)
