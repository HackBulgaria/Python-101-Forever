# ls.py
import sys
import os

show_hidden = len(sys.argv) > 1 and sys.argv[1] == "-a"

for directory_item in os.listdir("."):
    if directory_item.startswith("."):
        if not show_hidden:
            continue

    print(directory_item)
