"""
Write a script that finds log files (*.log) under /var/log (use pathlib).
If a log file is bigger than 100MB, compress it with shutil.make_archive() or move it to a backup folder.
"""

from pathlib import Path
import shutil
import sys

# Threshold: 100 MB
THRESHOLD = 100 * 1024 * 1024  # bytes
BACKUP_DIR = Path("/var/log/backup_logs")

def find_log_files():
    log_dir = Path("/var/log")

    if not log_dir.exists():
        print("Log directory does not exist.")
        sys.exit(1)

    if not BACKUP_DIR.exists():
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    for file in log_dir.rglob("*.log"):
        size = file.stat().st_size
        if size > THRESHOLD:
            print(f"Large log found: {file} ({size / (1024**2):.2f} MB)")
            handle_large_log(file)


def handle_large_log(file: Path):
    # Option 1: compress
    archive_name = BACKUP_DIR / file.stem  # no extension
    shutil.make_archive(str(archive_name), 'zip', root_dir=file.parent, base_dir=file.name)
    print(f"Compressed {file} -> {archive_name}.zip")

    # Option 2: move instead of compress
    # backup_path = BACKUP_DIR / file.name
    # shutil.move(str(file), backup_path)
    # print(f"Moved {file} -> {backup_path}")


if __name__ == "__main__":
    find_log_files()