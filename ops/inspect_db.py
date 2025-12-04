import sqlite3
import os
import sys

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'app.db')

def inspect_db():
    print(f"Inspecting database at: {DB_PATH}")
    
    if not os.path.exists(DB_PATH):
        print("Error: Database file not found.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("No tables found in the database.")
            return

        print(f"Found {len(tables)} tables.")

        for table in tables:
            table_name = table[0]
            if table_name == 'alembic_version':
                continue
                
            print(f"\n{'='*50}")
            print(f"Table: {table_name}")
            print(f"{'='*50}")

            # Get column names
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [info[1] for info in cursor.fetchall()]
            print(f"Columns: {', '.join(columns)}")
            print(f"{'-'*50}")

            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"Total Rows: {count}")

            # Get data (limit to 50 for readability)
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 50")
            rows = cursor.fetchall()

            if rows:
                print(f"First 50 rows:")
                for row in rows:
                    print(row)
            else:
                print("No data.")

        conn.close()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_db()
