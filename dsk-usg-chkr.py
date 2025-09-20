"""
Use shutil.disk_usage() to check free/used disk space.
Print an alert if free space is < 20%.
"""

import shutil
from pathlib import Path
import time
import sys
