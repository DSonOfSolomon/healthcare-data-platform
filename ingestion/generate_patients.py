# pandas is used to create and export datasets
import pandas as pd

# random is used to generate sample values
import random

# uuid creates unique identifiers
import uuid

# import project configuration
import config


# how many patients to generate
NUM_PATIENTS = 500


# possible genders
genders = ["Male", "Female"]


# possible regions patients might come from
regions = ["North", "South", "East", "West"]


# store generated patients
records = []


for _ in range(NUM_PATIENTS):

    record = {
        # unique patient identifier
        "patient_id": f"P{random.randint(1000,9999)}",

        # simulated demographic data
        "gender": random.choice(genders),

        # birth year for age calculations
        "birth_year": random.randint(1940, 2022),

        # geographic region
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