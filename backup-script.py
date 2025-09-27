"""
Use shutil to copy important config files (e.g., /etc/ssh/sshd_config) to a timestamped backup directory.
Add command-line arguments (via sys.argv) for source and destination.
"""

import shutil
import time
import sys
import os

def backup_file(source_file, backup_dir):
    """
    Copies a source file to a timestamped backup directory.
    """
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' not found.")
        return

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(source_file)}-{timestamp}")

    try:
        shutil.copy2(source_file, backup_path)
        print(f"Successfully backed up '{source_file}' to '{backup_path}'")
    except Exception as e:
        print(f"Error backing up file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup-script.py <source_file> <backup_directory>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]
    backup_file(source, destination)