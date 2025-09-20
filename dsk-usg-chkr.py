import shutil
from pathlib import Path
import sys


def check_existence(path: Path):
    print(f"Checking existence of {path}...")
    if path.exists() and path.is_dir():
        print(f"{path} exists!")
        return True
    else:
        print(f"{path} not found or doesn't exist.")
        return False


def check_disk_usage(path: Path):
    usage = shutil.disk_usage(path)

    total, used, free = usage.total, usage.used, usage.free
    gb = 1024 ** 3
    total_gb, used_gb, free_gb = total / gb, used / gb, free / gb

    percent_free = (free / total) * 100

    print(f"\nDisk usage for {path}:")
    print(f"  Total: {total_gb:.2f} GB")
    print(f"  Used:  {used_gb:.2f} GB")
    print(f"  Free:  {free_gb:.2f} GB ({percent_free:.2f}%)")

    if percent_free < 20:
        print("WARNING: Free space is below 20%!")


if __name__ == "__main__":
    try:
        directory = input("Enter directory path to check: ")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(1)

    path = Path(directory).resolve()

    if check_existence(path):
        check_disk_usage(path)
