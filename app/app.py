# #Flask App Code (app/app.py)

# Ab ek Flask API banate hain jo trained model ko load kare aur POST request handle kare.

# File: app/app.py

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load trained Random Forest model
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'random_forest_model.pkl')
model = joblib.load(model_path)

# 🔹 Route 1: Home page (HTML Form)
@app.route('/')
def home():
    return render_template('index.html')


# 🔹 Route 2: API Endpoint (for Postman / external use)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = pd.DataFrame([data])
        prediction = model.predict(input_data)[0]
        result = "Approved" if prediction == 1 else "Rejected"
        
        return jsonify({
            "status": "success",
            "prediction": int(prediction),
            "message": f"Loan {result}"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


# 🔹 Route 3: Web form submission
@app.route('/predict_form', methods=['POST'])
def predict_form():
    try:
        # Get data from HTML form
        form_data = {
            "Gender": 1 if request.form['Gender'] == 'Male' else 0,
            "Married": 1 if request.form['Married'] == 'Yes' else 0,
            "Education": 1 if request.form['Education'] == 'Graduate' else 0,
            "Self_Employed": 1 if request.form['Self_Employed'] == 'Yes' else 0,
            "ApplicantIncome": float(request.form['ApplicantIncome']),
            "CoapplicantIncome": float(request.form['CoapplicantIncome']),
            "LoanAmount": float(request.form['LoanAmount']),
            "Loan_Amount_Term": float(request.form['Loan_Amount_Term']),
            "Credit_History": float(request.form['Credit_History']),
            "Property_Area": (
                0 if request.form['Property_Area'] == 'Rural' else
                1 if request.form['Property_Area'] == 'Semiurban' else 2
            )
        }

        # Convert into DataFrame for model input
        input_df = pd.DataFrame([form_data])

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Render HTML result page
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return render_template('result.html', prediction=None, error=str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
