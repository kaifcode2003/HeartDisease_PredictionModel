# ❤️ Heart Disease Prediction Model

A machine learning project that predicts the likelihood of heart disease using patient health data.  
The model is built using **Logistic Regression** and deployed with a simple **Streamlit web app** for real-time predictions.  

---

## 📌 Project Overview

Heart disease is one of the leading causes of mortality worldwide. Early prediction can save lives by prompting timely medical intervention.  
This project leverages a dataset of patient health indicators (such as age, blood pressure, cholesterol levels, chest pain type, etc.) to predict whether a person is at risk of heart disease.  

The repository contains:
- A **Jupyter Notebook** for data analysis, preprocessing, and model training.
- Pre-trained model files (`.pkl`) for direct use.
- A **Streamlit app** (`app.py`) to interact with the model.

---

## 📂 Repository Structure



├── HeartDisease_PredictionModel.ipynb # Notebook with EDA and model training
├── app.py # Streamlit app for prediction
├── heart.csv # Dataset
├── Logistic_Regression.pkl # Saved Logistic Regression model
├── heart_scaler.pkl # Saved StandardScaler
├── heart_columns.pkl # Feature column list
└── README.md # Project documentation


---

## ✨ Features

- Exploratory Data Analysis (EDA) to understand dataset patterns  
- Logistic Regression classifier for prediction  
- Preprocessing with scaling for consistency  
- Real-time prediction interface using **Streamlit**  
- Demo options for both **High Risk** and **Low Risk** results  

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed.

### Installation

Clone the repository:
bash
git clone https://github.com/kaifcode2003/HeartDisease_PredictionModel.git
cd HeartDisease_PredictionModel


Install dependencies:

pip install -r requirements.txt

▶️ Usage
Run the Notebook

For training or exploration:

jupyter notebook HeartDisease_PredictionModel.ipynb

Run the Web App

To launch the prediction interface:

streamlit run app.py


Open the provided localhost link in your browser.

🧑‍💻 Demo Inputs
Example: Low Risk
Age: 30
Sex: Male
Chest Pain Type: 0
Blood Pressure: 120
Cholesterol: 200
Fasting Blood Sugar: 0
Resting ECG: 1
Max Heart Rate: 170
Exercise Angina: 0
Oldpeak: 0.5
Slope: 2
Major Vessels: 0
Thal: 2

Example: High Risk
Age: 65
Sex: Male
Chest Pain Type: 3
Blood Pressure: 160
Cholesterol: 300
Fasting Blood Sugar: 1
Resting ECG: 2
Max Heart Rate: 110
Exercise Angina: 1
Oldpeak: 2.5
Slope: 0
Major Vessels: 2
Thal: 3

📊 Model Details

Algorithm: Logistic Regression

Scaler: StandardScaler

Accuracy: (update with your notebook results)

Input Features: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal

🛠 Tech Stack

Python

Scikit-learn

Pandas & NumPy

Streamlit

Joblib

🤝 Contributing

Fork this repo

Create a feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Added feature")

Push to your branch (git push origin feature-name)

Open a Pull Request

📜 License

This project is licensed under the MIT License.

👨‍💻 Developed By

Mohd Kaif
B.Tech Electronics & Communication Engineering (AI & ML Specialization)
MIT World Peace University, Pune
