import pandas as pd

# load datasets
patients = pd.read_csv("data/raw/patients.csv")
admissions = pd.read_csv("data/raw/patient_admissions.csv")

# convert to sets for comparison
patient_ids = set(patients["patient_id"])
admission_patient_ids = set(admissions["patient_id"])

# find IDs in admissions that don't exist in patients
missing = admission_patient_ids - patient_ids

print("Missing patient IDs:", missing)