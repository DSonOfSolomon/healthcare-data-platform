import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import random

NUM_RECORDS = 500

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
            "patient_id": f"P{random.randint(1000,9999)}",
            "hospital_id": random.choice(hospitals),
            "department": random.choice(departments),
            "admission_time": admission_time,
            "admission_type": random.choice(["emergency","scheduled"]),
            "created_at": datetime.now()
        }

        records.append(record)

    df = pd.DataFrame(records)

    df.to_csv(
        "data/raw/patient_admissions.csv",
        index=False
    )

    print("Generated patient admissions dataset")

if __name__ == "__main__":
    generate_admissions()