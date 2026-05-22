import pandas as pd

from configs.db import get_engine

engine = get_engine()

data = {
    "authority_name": [
        "Bath and North East Somerset",
        "Bristol City Council",
        "Cardiff Council",
    ],
    "dataset_topic": [
        "EV Chargers",
        "Potholes",
        "Flood Incidents",
    ],
}

df = pd.DataFrame(data)

df.to_sql(
    "sample_datasets",
    engine,
    schema="raw",
    if_exists="replace",
    index=False,
)

print("Data loaded successfully.")