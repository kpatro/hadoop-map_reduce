#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)

for line in sys.stdin:
    row = line.strip()
    cols = row.split(",")
    x = (str(cols[2]) + str(cols[3])).replace(')', '').replace("'", "").strip()
    print(x, 1)