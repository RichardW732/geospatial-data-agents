from datetime import datetime

from sqlalchemy import text

from configs.db import get_engine


def log_ingestion_run(
    source_name: str,
    target_table: str,
    row_count: int,
    status: str = "success",
    notes: str | None = None,
):
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO metadata.ingestion_runs (
                    source_name,
                    target_table,
                    row_count,
                    completed_at,
                    status,
                    notes
                )
                VALUES (
                    :source_name,
                    :target_table,
                    :row_count,
                    :completed_at,
                    :status,
                    :notes
                )
            """),
            {
                "source_name": source_name,
                "target_table": target_table,
                "row_count": row_count,
                "completed_at": datetime.now(),
                "status": status,
                "notes": notes,
            },
        )