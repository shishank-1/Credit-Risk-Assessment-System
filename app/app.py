# #Flask App Code (app/app.py)

# Ab ek Flask API banate hain jo trained model ko load kare aur POST request handle kare.

# File: app/app.py

from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained Random Forest model
import os
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'random_forest_model.pkl')
model = joblib.load(model_path)


@app.route('/')
def home():
    return jsonify({"message": "Credit Risk Assessment API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Convert incoming data into DataFrame
        input_data = pd.DataFrame([data])
        
        # Predict using loaded model
        prediction = model.predict(input_data)[0]
        
        # Convert numeric output to text
        result = "Approved" if prediction == 1 else "Rejected"
        
        return jsonify({
            "status": "success",
            "prediction": int(prediction),
            "message": f"Loan {result}"
        })
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
