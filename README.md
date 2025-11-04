Credit Risk Assessment System

Live Website: https://web-production-bc4aa.up.railway.app/

🎯 Project Overview

The Credit Risk Assessment System predicts whether a loan applicant is likely to default or get approval using Machine Learning.
It analyzes applicant income, employment, education, credit history, and property details to assist banks in data-driven lending decisions.

⚙️ Tech Stack

Frontend: HTML5, CSS3 (Responsive Design)

Backend: Flask (Python)

Machine Learning: Scikit-learn (Random Forest)

Database: SQLite

Deployment Platform: Railway

🧾 Project Conventions & Metadata
1️⃣ Target Variable

Name: Loan_Status

Meaning:

1 → Loan Approved / Likely to Repay

0 → Loan Rejected / Likely to Default

Conversion (if categorical):

Y → 1

N → 0

2️⃣ Data Format Standards

ApplicantIncome: Monthly income of the main applicant (example: ₹50,000)
CoapplicantIncome: Monthly income of the co-applicant (example: ₹25,000)
LoanAmount: Loan amount requested (in thousands, e.g., 200 = ₹200,000)
Loan_Amount_Term: Repayment duration in months (e.g., 360 = 30 years)
Credit_History: Credit score flag (1 = good, 0 = bad)
Property_Area: Encoded (0 = Rural, 1 = Semiurban, 2 = Urban)
Education: Encoded (0 = Not Graduate, 1 = Graduate)
Self_Employed: Encoded (0 = No, 1 = Yes)

Note: There are no date columns in the dataset. If added later, the standard format will be YYYY-MM-DD.

3️⃣ Model & Randomization Settings

Random Seed: RANDOM_STATE = 42

Model Used: Random Forest Classifier

Evaluation Metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC

4️⃣ Git Branching Convention

Main Branch: main – Stable production-ready code used for deployment
Development Branch: dev/eda – Used for exploratory data analysis and feature engineering
After testing, merge updates from dev/eda to main.

5️⃣ Deployment Information

Platform: Railway
URL: https://web-production-bc4aa.up.railway.app/

App Type: Flask-based web application
Frontend: HTML5 and CSS3 with responsive design
Backend: Flask + Python API for real-time predictions
Model Storage: random_forest_model.pkl file located in the /models/ directory

6️⃣ Project Features

Data Cleaning and Feature Engineering using Pandas

Model Training using Random Forest Classifier

REST API for Real-Time Loan Predictions

Interactive Web Interface for User Input

Responsive Design for Desktop and Mobile

7️⃣ Setup Instructions (Local Development)

Clone the repository

git clone https://github.com/shishank-1/Credit-Risk-Assessment-System.git
cd Credit-Risk-Assessment-System


Create a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run Flask server

python app/app.py


Open browser and go to:
http://127.0.0.1:5000/

8️⃣ Developer Credit

Developed by: Shishank
Focus Areas: Data Analytics, Machine Learning, and Model Deployment

🧠 Future Enhancements

Integrate model explainability tools like SHAP or LIME

Add credit score API integration

Include an admin dashboard for monitoring loan predictions

Automate CI/CD deployment pipeline
