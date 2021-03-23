#!/usr/bin/env python
import sys
import re

# maps makeyear to count
makeyear = {}
sm = 0
for line in sys.stdin:
    rows = line.split(",")
    cols = rows[0].replace("'","").replace("(","")
    ct = int(rows[1].strip().replace(")",""))
    # print(cols, ct)
    temp = re.findall(r'\d+', cols)

    for i, val in enumerate(temp):
        try:
            makeyear[cols] = makeyear[cols] + ct
        except:
            makeyear[cols] = ct

print(makeyear)