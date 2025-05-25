import sys
import os
import sqlite3 
from lib.db.connection import get_connection


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def setup_db():
    schema_path = "lib/db/schema.sql" 
    conn = None  
    try:
        print(f"Attempting to open schema file: {schema_path}")
        
        full_schema_path = os.path.join(project_root, schema_path)
        with open(full_schema_path) as f:
            schema = f.read()
        print("Schema file read successfully.")

        print("Attempting to get database connection...")
        conn = get_connection()
        print("Database connection obtained.")

        print("Attempting to execute schema...")
        conn.executescript(schema)
        print("Schema executed successfully.")

        conn.commit()
        print("Database changes committed.")

    except FileNotFoundError:
        print(f"ERROR: Schema file not found at {full_schema_path}.")
        print("Make sure 'lib/db/schema.sql' exists in your project root and you are running this script correctly.")
    except sqlite3.Error as e:
        print(f"ERROR: An SQLite error occurred: {e}")
        if conn:
            print("Rolling back any pending changes.")
            conn.rollback()
    except ImportError as e:
        print(f"ERROR: Could not import a required module: {e}")
        print("Please ensure all dependencies are installed and your project structure is correct.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    print("Setting up the database...")
    setup_db()
    print("Database setup process finished.")

