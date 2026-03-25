import pandas as pd
import random
from datetime import datetime, timedelta
import uuid
import config


# load datasets
patients_df = pd.read_csv("data/raw/patients.csv")
patient_ids = patients_df["patient_id"].tolist()

hospitals_df = pd.read_csv("data/raw/hospitals.csv")
hospital_ids = hospitals_df["hospital_id"].tolist()

departments_df = pd.read_csv("data/raw/departments.csv")
department_ids = departments_df["department_id"].tolist()

admissions_df = pd.read_csv("data/raw/patient_admissions.csv")
admission_ids = admissions_df["admission_id"].tolist()


NUM_RECORDS = 200

treatment_types = [
    "Surgery",
    "Medication",
    "Therapy",
    "Diagnostic"
]

records = []

for _ in range(NUM_RECORDS):

    treatment_time = datetime.now() - timedelta(
        days=random.randint(0, 30)
    )

    record = {
        "treatment_id": str(uuid.uuid4()),

        # link to existing entities
        "patient_id": random.choice(patient_ids),
        "hospital_id": random.choice(hospital_ids),
        "department_id": random.choice(department_ids),
        "admission_id": random.choice(admission_ids),

        # treatment info
        "treatment_type": random.choice(treatment_types),
        "treatment_cost": random.randint(100, 5000),
        "treatment_time": treatment_time,

        "created_at": datetime.now()
    }

    records.append(record)


df = pd.DataFrame(records)

df.to_csv(
    f"{config.RAW_DATA_PATH}/treatments.csv",
    index=False
)

print("treatments dataset generated")