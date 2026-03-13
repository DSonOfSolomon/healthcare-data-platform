import pandas as pd
import random
import uuid
import config


NUM_PATIENTS = 500

genders = ["Male", "Female"]
regions = ["North", "South", "East", "West"]


# store generated patients
records = []


for _ in range(NUM_PATIENTS):

    record = {
        # unique patient identifier
        "patient_id": f"P{random.randint(1000,9999)}",

        "gender": random.choice(genders),

        "birth_year": random.randint(1940, 2022),

        "region": random.choice(regions)
    }

    records.append(record)


# convert to dataframe
df = pd.DataFrame(records)


# save dataset to raw data folder
df.to_csv(
    f"{config.RAW_DATA_PATH}/patients.csv",
    index=False
)


print("patients dataset generated")