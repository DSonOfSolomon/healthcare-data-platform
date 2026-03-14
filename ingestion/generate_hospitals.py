# pandas for creating datasets
import pandas as pd

# import project configuration
import config


# predefined hospitals for the platform
hospitals = [
    {"hospital_id": "HOSP01", "hospital_name": "North General Hospital", "city": "Manchester", "capacity": 450},
    {"hospital_id": "HOSP02", "hospital_name": "City Medical Centre", "city": "London", "capacity": 620},
    {"hospital_id": "HOSP03", "hospital_name": "Riverside Hospital", "city": "Birmingham", "capacity": 380},
    {"hospital_id": "HOSP04", "hospital_name": "St Mary’s Medical", "city": "Leeds", "capacity": 510}
]


# convert list of dictionaries into a dataframe
df = pd.DataFrame(hospitals)


# save dataset to raw data folder
df.to_csv(
    f"{config.RAW_DATA_PATH}/hospitals.csv",
    index=False
)


print("hospitals dataset generated")