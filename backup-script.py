"""
Use shutil to copy important config files (e.g., /etc/ssh/sshd_config) to a timestamped backup directory.
Add command-line arguments (via sys.argv) for source and destination.
"""

import shutil
import time
import sys
