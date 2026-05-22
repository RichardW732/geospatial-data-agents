import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

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