"""
Use shutil.disk_usage() to check free/used disk space.
Print an alert if free space is < 20%.
"""

import shutil
from pathlib import Path
import time
import sys

try:
    directory = (input("Enter name of directory to be checked: "))
    print("Be sure to enter a string value.")
except KeyboardInterrupt:
    print("Program failed. The process was interrupted by the user. ")
    sys.exit[1]

path = Path(str(directory)).resolve()


def existence_checker(path):
    print(f"Initiating search for {path}")
    
    start = time.time()

    home_dir = Path.home()
    found = False

    for item in home_dir.iterdir():
        if path.exists() and path.is_dir():
            print(f"{path} exists! ")
            found = True
        if not found:
            print(f"{path} not found or doesn't exist. ")

    end = time.time()
    total = end - start
    print(f"Time verifying path existence: {total}")


def disk_usage(path):
    print(f"Initiating disk usage checking for {path}")
    start = time.time()
    usage = shutil.disk_usage(path)

    # Extract values (in bytes)
    total = usage.total
    used = usage.used
    free = usage.free

    # Convert to GB for readability
    gb = 1024 ** 3
    total_gb = total / gb
    used_gb = used / gb
    free_gb = free / gb

    # Print results
    print(f"Disk usage for {path}:")
    print(f"  Total: {total_gb:.2f} GB")
    print(f"  Used:  {used_gb:.2f} GB")
    print(f"  Free:  {free_gb:.2f} GB")

    # Warning if less than 10% free
    if free / total < 0.20:
        print("WARNING: Free space is below 10%!")
    
    end = time.time()
    total = end - start
    print(f"Time reading disk usage: {total}")

existence_checker(path)
disk_usage(path)
