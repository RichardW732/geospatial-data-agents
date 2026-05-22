from sqlalchemy import create_engine, text

# Replace with your actual password
PASSWORD = "p8jIpptKI3bDz3si"

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"postgres.hpxvjfowkzxpvetckrkw:{PASSWORD}"
    f"@aws-1-eu-west-2.pooler.supabase.com:5432/postgres"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))

    for row in result:
        print(row)