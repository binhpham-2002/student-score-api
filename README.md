# 🎓 Student Score Prediction API

An end-to-end Machine Learning system for predicting student academic performance using supervised learning models and serving real-time inference via FastAPI.

---

## 🚀 Project Overview

This project demonstrates the design and deployment of a production-ready ML system:

- Data preprocessing pipeline (scikit-learn)
- Supervised regression model
- Model serialization using joblib
- RESTful API using FastAPI
- Containerization with Docker
- Cloud deployment

---

## 🧠 Problem Statement

Predict student final scores based on:

- Academic behavior (hours studied, attendance)
- Lifestyle factors (sleep, physical activity)
- Socioeconomic features (family income, internet access)
- Psychological indicators (motivation level, peer influence)

---

## 🛠 Tech Stack

- Python
- Scikit-learn
- Pandas
- FastAPI
- Uvicorn
- Docker

---

## 🏗 Architecture

Client → FastAPI → ML Pipeline → Prediction → JSON Response

---

## 📊 Model Pipeline

- Numerical preprocessing
- Categorical encoding
- Random Forest Regressor
- Unified scikit-learn Pipeline

---

## 📡 API Endpoints

### GET /
Returns API status message

### GET /health
Health check endpoint

### POST /predict
Predict student score

Example Request:

```json
{
  "Hours_Studied": 10,
  "Attendance": 85,
  "Sleep_Hours": 7,
  "Previous_Scores": 75,
  "Tutoring_Sessions": 2,
  "Physical_Activity": 3,
  "Parental_Involvement": "High",
  "Access_to_Resources": "Medium",
  "Extracurricular_Activities": "Yes",
  "Motivation_Level": "High",
  "Internet_Access": "Yes",
  "Family_Income": "Low",
  "School_Type": "Public",
  "Peer_Influence": "Positive",
  "Learning_Disabilities": "No",
  "Gender": "Male"
}
## 🌍 Live Demo
https://student-score-api.onrender.com/docs