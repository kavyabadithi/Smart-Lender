from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/loan_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    input_data = {
        "Gender": request.form["Gender"],
        "Married": request.form["Married"],
        "Education": request.form["Education"],
        "Self_Employed": request.form["Self_Employed"],
        "ApplicantIncome": float(request.form["ApplicantIncome"]),
        "CoapplicantIncome": float(request.form["CoapplicantIncome"]),
        "LoanAmount": float(request.form["LoanAmount"]),
        "Loan_Amount_Term": float(request.form["Loan_Amount_Term"]),
        "Credit_History": request.form["Credit_History"],
        "Property_Area": request.form["Property_Area"]
    }

    features = []
    for key in [
        "Gender", "Married", "Education", "Self_Employed",
        "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
        "Loan_Amount_Term", "Credit_History", "Property_Area"
    ]:
        if key in label_encoders:
            features.append(label_encoders[key].transform([input_data[key]])[0])
        else:
            features.append(input_data[key])

    prediction = model.predict([features])

    if prediction[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)