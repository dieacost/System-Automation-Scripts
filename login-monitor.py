"""
Use subprocess to run who or last and parse output.
Detect if a login comes from outside a trusted IP range (simulate whitelist).
"""

import subprocess
import ipaddress
import re

# Define whitelist ranges
whitelist = [
    ipaddress.ip_network("192.168.1.0/24"),
    ipaddress.ip_network("10.0.0.0/8")
]

def is_whitelisted(ip, whitelist):
    ip_obj = ipaddress.ip_address(ip)
    return any(ip_obj in net for net in whitelist)

# Run 'who'
result = subprocess.run(["who"], capture_output=True, text=True)
lines = result.stdout.strip().split("\n")

for line in lines:
    match = re.search(r"\(([\d\.]+)\)", line)
    if match:
        ip = match.group(1)
        if is_whitelisted(ip, whitelist):
            print(f"{ip} is ALLOWED")
        else:
            print(f"{ip} is BLOCKED")