"""
Write a script that finds log files (*.log) under /var/log (use pathlib).
If a log file is bigger than 100MB, compress it with shutil.make_archive() or move it to a backup folder.
"""

from pathlib import Path
import time
import shutil
import sys

