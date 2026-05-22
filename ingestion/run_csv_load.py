from ingestion.csv_loader import load_csv_to_postgres

load_csv_to_postgres(
    csv_path="raw_data/sample_foi_data.csv",
    table_name="foi_sample_csv",
)