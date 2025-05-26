# run_queries.py

from lib.db.connection import get_connection

def run_query(sql, params=None):
    """Execute a given SQL query with optional parameters."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
        return cursor.fetchall()
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    query = "SELECT * FROM articles;"  # Replace with your table name
    results = run_query(query)
    for row in results:
        print(row)
