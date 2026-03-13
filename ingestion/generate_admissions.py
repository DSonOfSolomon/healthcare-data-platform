import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import random
import config




patients_df = pd.read_csv("data/raw/patients.csv")

patient_ids = patients_df["patient_id"].tolist()


NUM_RECORDS = config.NUM_ADMISSIONS

hospitals = ["HOSP01", "HOSP02", "HOSP03"]
departments = ["Emergency", "Cardiology", "Surgery", "ICU"]

def generate_admissions():

    records = []

    for _ in range(NUM_RECORDS):

        admission_time = datetime.now() - timedelta(
            hours=random.randint(0, 72)
        )

        record = {
            "admission_id": str(uuid.uuid4()),
            "patient_id": random.choice(patient_ids),
            "hospital_id": random.choice(hospitals),
            "department": random.choice(departments),
            "admission_time": admission_time,
            "admission_type": random.choice(["emergency","scheduled"]),
            "created_at": datetime.now()
        }

        records.append(record)

    df = pd.DataFrame(records)

    df.to_csv(
        f"{config.RAW_DATA_PATH}/patient_admissions.csv",
        index=False
    )

    print("Generated patient admissions dataset")

if __name__ == "__main__":
    generate_admissions()