# pandas is used to create datasets
import pandas as pd

# import project configuration
import config


# predefined hospital departments
departments = [
    {"department_id": "DEPT01", "department_name": "Emergency"},
    {"department_id": "DEPT02", "department_name": "Cardiology"},
    {"department_id": "DEPT03", "department_name": "ICU"},
    {"department_id": "DEPT04", "department_name": "Surgery"},
    {"department_id": "DEPT05", "department_name": "Orthopedics"}
]


# convert to dataframe
df = pd.DataFrame(departments)


# save dataset
df.to_csv(
    f"{config.RAW_DATA_PATH}/departments.csv",
    index=False
)


print("departments dataset generated")