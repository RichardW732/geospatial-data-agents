import pandas as pd
from sqlalchemy import create_engine

PASSWORD = "p8jIpptKI3bDz3si"

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"postgres.hpxvjfowkzxpvetckrkw:{PASSWORD}"
    f"@aws-1-eu-west-2.pooler.supabase.com:5432/postgres"
)

engine = create_engine(DATABASE_URL)

data = {
    "authority_name": [
        "Bath and North East Somerset",
        "Bristol City Council",
        "Cardiff Council"
    ],
    "dataset_topic": [
        "EV Chargers",
        "Potholes",
        "Flood Incidents"
    ]
}

df = pd.DataFrame(data)

df.to_sql(
    "sample_datasets",
    engine,
    schema="raw",
    if_exists="replace",
    index=False
)

print("Data loaded successfully.")