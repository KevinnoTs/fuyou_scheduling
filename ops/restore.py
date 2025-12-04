import os
import shutil
import glob

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'app.db')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

def restore_db():
    print(f"Starting restore process...")
    
    if not os.path.exists(BACKUP_DIR):
        print(f"Error: Backup directory not found at {BACKUP_DIR}")
        return

    backups = glob.glob(os.path.join(BACKUP_DIR, '*.db'))
    if not backups:
        print("No backup files found.")
        return

    # Sort backups by modification time (newest first)
    backups.sort(key=os.path.getmtime, reverse=True)

    print("\nAvailable backups:")
    for i, backup in enumerate(backups):
        filename = os.path.basename(backup)
        # Get file size in KB
        size_kb = os.path.getsize(backup) / 1024
        # Get modification time
        mtime = os.path.getmtime(backup)
        mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"{i + 1}. {filename} ({size_kb:.1f} KB) - {mtime_str}")

    try:
        choice = input("\nEnter the number of the backup to restore (or 'q' to quit): ")
        if choice.lower() == 'q':
            return

        index = int(choice) - 1
        if 0 <= index < len(backups):
            selected_backup = backups[index]
            print(f"\nSelected backup: {selected_backup}")
            print(f"Target database: {DB_PATH}")
            
            # Confirm
            confirm = input(f"WARNING: This will overwrite the current database. Continue? (y/n): ")
            if confirm.lower() != 'y':
                print("Restore cancelled.")
                return

            # Create a safety backup of current state before restoring
            if os.path.exists(DB_PATH):
                print("Creating safety backup of current state...")
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                safety_backup = os.path.join(BACKUP_DIR, f"safety_backup_before_restore_{timestamp}.db")
                shutil.copy2(DB_PATH, safety_backup)
                print(f"Safety backup created: {safety_backup}")

            shutil.copy2(selected_backup, DB_PATH)
            print("Database successfully restored.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"Error restoring database: {e}")

import datetime # Added missing import

if __name__ == "__main__":
    restore_db()
