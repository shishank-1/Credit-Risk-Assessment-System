# 📘 Data Dictionary — Loan Dataset

This document describes each column in `loan_data.csv`, including type, meaning, and possible values.  
It serves as a reference for preprocessing, feature engineering, and model training.

---

| Column Name        | Description                                                | Type        | Possible Values / Units                 | Missing Values / Codes |
|--------------------|------------------------------------------------------------|-------------|-----------------------------------------|-------------------------|
| **Loan_ID**        | Unique identifier for each loan applicant *(not used in synthetic data, can be added if needed)* | Categorical | e.g., LP001002, LP001003                | None |
| **Gender**         | Gender of the applicant                                   | Categorical | Male / Female                           | None |
| **Married**        | Applicant’s marital status                                | Categorical | Yes / No                                | None |
| **Dependents**     | Number of dependents *(not included in synthetic data; can be added later)* | Categorical | 0 / 1 / 2 / 3+                          | None |
| **Education**      | Educational qualification of the applicant                | Categorical | Graduate / Not Graduate                 | None |
| **Self_Employed**  | Whether the applicant is self-employed                    | Categorical | Yes / No                                | None |
| **ApplicantIncome**| Monthly income of the applicant                           | Numeric     | In currency units (e.g., ₹ / $)         | None |
| **CoapplicantIncome** | Monthly income of co-applicant                         | Numeric     | In currency units (e.g., ₹ / $)         | None |
| **LoanAmount**     | Loan amount applied for                                   | Numeric     | In thousands (e.g., 100 = ₹100,000)     | None |
| **Loan_Amount_Term** | Loan repayment term                                    | Numeric     | In months (e.g., 120, 180, 240, 360)    | None |
| **Credit_History** | Credit repayment history of the applicant                 | Numeric     | 1.0 = Good credit history, 0.0 = Poor   | None |
| **Property_Area**  | Type of property area                                     | Categorical | Urban / Semiurban / Rural               | None |
| **Loan_Status**    | Loan status (target variable)                             | Binary (Int) | 1 = Approved/Repay, 0 = Default/Rejected | None |

---

### Notes:
- All fields are **synthetically generated**, no PII included.  
- `Loan_ID` and `Dependents` are *optional* and can be added in future versions.  
- No missing values exist in this dataset (can simulate for testing).  
- Column names follow `snake_case` for consistency in preprocessing scripts.  

---

**Version:** 1.0  
**Source:** Generated synthetically using NumPy & Pandas  
**Date:** 2025-11-04
