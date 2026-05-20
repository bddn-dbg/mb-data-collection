import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS workers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    photo TEXT,
    aadhaar VARCHAR(20),
    mobile VARCHAR(20),
    city VARCHAR(100),
    category VARCHAR(100),
    experience INTEGER,
    skills TEXT,
    address TEXT,
    description TEXT,
    rating FLOAT
)
""")

conn.commit()

cur.close()
conn.close()

print("✅ workers table created successfully")