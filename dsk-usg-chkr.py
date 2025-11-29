"""
Use shutil.disk_usage() to check free/used disk space.
Print an alert if free space is < 20%.
"""

import shutil

def check_disk_usage(disk):
    """Checks disk usage and prints an alert if free space is low."""
    total, used, free = shutil.disk_usage(disk)
    free_percent = (free / total) * 100
    
    print(f"Disk: {disk}")
    print(f"Total: {total / (1024**3):.2f} GB")
    print(f"Used: {used / (1024**3):.2f} GB")
    print(f"Free: {free / (1024**3):.2f} GB ({free_percent:.2f}%)")

    if free_percent < 20:
        print("Alert: Free space is less than 20%!")
    else:
        print("Disk space is sufficient.")

if __name__ == "__main__":
    check_disk_usage("/")
