# combined.py
import sys

for line in sys.stdin:
    if "And" in line:
        sys.stdout.write(line)
    else:
        sys.stderr.write(line)
