import pandas as pd
import random
from datetime import datetime, timedelta
import uuid
import config


# load reference datasets
patients_df = pd.read_csv("data/raw/patients.csv")
patient_ids = patients_df["patient_id"].tolist()

hospitals_df = pd.read_csv("data/raw/hospitals.csv")
hospital_ids = hospitals_df["hospital_id"].tolist()

departments_df = pd.read_csv("data/raw/departments.csv")
department_ids = departments_df["department_id"].tolist()


NUM_RECORDS = 200

records = []

for _ in range(NUM_RECORDS):

    appointment_time = datetime.now() + timedelta(
        days=random.randint(0, 30)
    )

    record = {
        "appointment_id": str(uuid.uuid4()),

        # link to existing entities
        "patient_id": random.choice(patient_ids),
        "hospital_id": random.choice(hospital_ids),
        "department_id": random.choice(department_ids),

        # appointment details
        "appointment_time": appointment_time,
        "status": random.choice(["scheduled", "completed", "cancelled"]),

        "created_at": datetime.now()
    }

    records.append(record)


df = pd.DataFrame(records)

df.to_csv(
    f"{config.RAW_DATA_PATH}/appointments.csv",
    index=False
)

print("appointments dataset generated")