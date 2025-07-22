# 🫀 Heart Failure Prediction Web App

A Flask-based web application that predicts the likelihood of heart failure using patient clinical data. The model was trained using a logistic regression algorithm, chosen for its superior generalization performance on this dataset.

---

## 🔍 Overview

This project leverages machine learning to assist medical professionals in identifying patients at risk of heart failure based on clinical records. The web interface allows users to input patient details and receive an instant prediction.

- *Frontend*: HTML with Bootstrap styling  
- *Backend*: Flask  
- *Model*: Logistic Regression (trained using Scikit-learn)  
- *Scaler*: StandardScaler for input normalization  

---

## 🧠 Dataset

- *Source*: Heart Failure Clinical Records Dataset  
- *Samples*: 299 
- *Target Variable*: DEATH_EVENT (0 = survived, 1 = died)  

---

## ⚙️ How to Run the App

1. *Clone this repository or download the files*

2. *Install dependencies*:
   bash
   pip install -r requirements.txt
   
3. *Run the Flask app*:
   bash
   python app.py
   
4. *Open your browser and visit*: http://127.0.0.1:5000/
