#!/usr/bin/env python
import sys

# with open("data.csv", "r") as f:
#     print(f.read())

# input comes from STDIN (standard input)
accidents = {}
key = []
values = []
for line in sys.stdin:
    row = line.strip()
    cols = row.split(",")
    print("{}\t{},{},{}".format(cols[2], cols[1], cols[3], cols[5]))
