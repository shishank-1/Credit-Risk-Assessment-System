import csv
import random
import numpy as np

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define possible values
genders = ['Male', 'Female']
married_status = ['Yes', 'No']
education = ['Graduate', 'Not Graduate']
self_employed = ['Yes', 'No']
property_areas = ['Urban', 'Semiurban', 'Rural']
loan_terms = [120, 180, 240, 360]  # days

# Generate 1000+ rows
num_rows = 1000

data = []
data.append(['Gender', 'Married', 'Education', 'Self_Employed', 'ApplicantIncome', 
             'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 
             'Property_Area', 'Loan_Status'])

for i in range(num_rows):
    gender = random.choice(genders)
    married = random.choice(married_status)
    education_level = random.choice(education)
    self_emp = random.choice(self_employed)
    property_area = random.choice(property_areas)
    
    # Generate realistic income based on education and employment
    if education_level == 'Graduate':
        base_income = random.randint(3000, 50000)
    else:
        base_income = random.randint(2000, 35000)
    
    if self_emp == 'Yes':
        applicant_income = int(base_income * random.uniform(0.8, 1.2))
    else:
        applicant_income = int(base_income * random.uniform(0.9, 1.3))
    
    # Coapplicant income (lower if married, might be 0 if single)
    if married == 'Yes':
        coapplicant_income = random.randint(0, int(applicant_income * random.uniform(0.3, 1.0)))
    else:
        coapplicant_income = random.randint(0, int(applicant_income * random.uniform(0.0, 0.5)))
    
    # Loan amount related to income
    total_income = applicant_income + coapplicant_income
    loan_amount = random.randint(int(total_income * 0.5), int(total_income * 2.5))
    loan_amount = min(loan_amount, 1000)  # Cap at reasonable value
    
    # Loan term
    loan_term = random.choice(loan_terms)
    
    # Credit history (1.0 or 0.0)
    credit_history = 1.0 if random.random() > 0.15 else 0.0
    
    # Loan status - influenced by credit history, income ratio, and other factors
    income_ratio = loan_amount / total_income if total_income > 0 else 10
    if credit_history == 1.0 and income_ratio < 5 and applicant_income > 5000:
        loan_status = 1 if random.random() > 0.2 else 0
    elif credit_history == 0.0:
        loan_status = 1 if random.random() > 0.7 else 0
    else:
        loan_status = 1 if random.random() > 0.5 else 0
    
    data.append([
        gender,
        married,
        education_level,
        self_emp,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area,
        loan_status
    ])

# Write to CSV file
output_file = r'C:\Users\shishank_1\Desktop\Credit Risk Assessment System\data\raw\loan_data.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Generated {num_rows} rows of loan data and saved to {output_file}")


