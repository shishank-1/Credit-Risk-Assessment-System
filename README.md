# Credit Risk Assessment System

## 🎯 Project Conventions & Metadata

### Target Variable
- **Name:** `Loan_Status`  
- **Meaning:** 1 = Loan approved/repay, 0 = Loan default/rejected  
- If dataset uses Y/N, convert using:
Y → 1
N → 0

### Data Formats
- **Date Format:** No date fields in current dataset (YYYY-MM-DD format will be used if added later).  
- **Currency / Units:**
- `ApplicantIncome`, `CoapplicantIncome` → Monthly income (in currency units)
- `LoanAmount` → Amount in *thousands* (e.g., 200 = ₹200,000)
- `Loan_Amount_Term` → Duration in *months* (e.g., 360 months = 30 years)

### Random Seed / Reproducibility
- **RANDOM_STATE:** `42`  
(Used for train-test split, RandomForest classifier, and other random operations to keep results consistent.)

### Branching Convention (Git)
- **Main branch:** `main` → Stable production-ready code  
- **Development branch:** `dev/eda` → For exploratory data analysis and preprocessing  
- Work on this branch during experimentation  
- Merge into `main` once results are validated

### Folder Structure Reminder
data/
├── raw/
├── processed/
src/
├── data/
├── models/
├── app/
notebooks/
├── 01_EDA_and_Preprocessing.ipynb


---

## 📅 Metadata Summary
- **Dataset Source:** Synthetic dataset generated using NumPy & Pandas  
- **Version:** 1.0  
- **Created On:** 2025-11-04  
- **Author:** Shadow (Project Owner)
