# Smart Lender - AI Powered Loan Prediction System

## Overview
Smart Lender is a Machine Learning based web application that predicts whether a loan should be approved or rejected based on applicant details.

## Features

- Loan Eligibility Prediction
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost (Best Model)
- Flask Web Application
- User Friendly Interface

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- HTML
- CSS

## Project Structure

```
Smart-Lender/
│── app.py
│── train_model.py
│── dataset.csv
│── loan_model.pkl
│── label_encoders.pkl
│── requirements.txt
│── README.md
│
├── templates/
│     ├── index.html
│     └── result.html
│
└── static/
      └── style.css
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```
----------------------------------------------------------------
💻Team Members
  Kavyasri Badithi
  kavyabadithi@gmail.com

  💻keerthika Bandreddy
     keerthikabandreddy@gmail.com

  💻Mudragalla Kowshik Kumar
    kkowshik994@gmail.com

  💻Kottu Akshara
    kottuakshara@gmail.com

  💻Lavanya Lahari Chukka  
    laharichukka@gmail.com

  ---------------------------------------------------------------  

  🎯CONCLUSION.....
     Smart Lender is a machine learning-powered web application that automates and accelerates the loan approval process for financial institutions. By evaluating key applicant data through various classification models, the XGBoost algorithm emerged as the top performer, achieving a high 94.7% training accuracy and 81.1% testing accuracy. Seamlessly integrated into a user-friendly Flask web interface, this predictive system allows credit officers to input applicant details and instantly receive real-time approval predictions. Ultimately, this digital solution streamlines banking operations by fast-tracking low-risk applications while proactively mitigating financial risks by flagging high-risk defaults.