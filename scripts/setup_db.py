import sqlite3
from lib.db.connection import get_connection

def setup_db():
    with open("lib/db/schema.sql") as f:
        schema = f.read()
    conn = get_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_db()
