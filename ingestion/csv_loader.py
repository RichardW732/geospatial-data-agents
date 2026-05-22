import pandas as pd

from configs.db import get_engine
from ingestion.metadata_logger import log_ingestion_run


def load_csv_to_postgres(
    csv_path: str,
    table_name: str,
    schema: str = "raw",
    if_exists: str = "replace",
):
    engine = get_engine()

    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        engine,
        schema=schema,
        if_exists=if_exists,
        index=False,
    )

    log_ingestion_run(
        source_name=csv_path,
        target_table=f"{schema}.{table_name}",
        row_count=len(df),
    )

    print(f"Loaded {len(df)} rows into {schema}.{table_name}")