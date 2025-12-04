import os
import shutil
import datetime

# Define paths
# This script is in fuyou_scheduling/ops/
# We need to go up one level to get to fuyou_scheduling/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'app.db')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

def backup_db():
    print(f"Starting backup process...")
    print(f"Base Directory: {BASE_DIR}")
    
    if not os.path.exists(BACKUP_DIR):
        try:
            os.makedirs(BACKUP_DIR)
            print(f"Created backup directory: {BACKUP_DIR}")
        except OSError as e:
            print(f"Error creating backup directory: {e}")
            return

    if not os.path.exists(DB_PATH):
        print(f"Error: Database file not found at {DB_PATH}")
        return

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"app_backup_{timestamp}.db"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    try:
        shutil.copy2(DB_PATH, backup_path)
        print(f"Successfully backed up database to: {backup_path}")
    except Exception as e:
        print(f"Error backing up database: {e}")

if __name__ == "__main__":
    backup_db()
