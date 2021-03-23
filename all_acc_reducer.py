#!/usr/bin/env python
import sys

# [Define group level master information]
# vins = set()
# for line in sys.stdin:
#     line = line.split('\t')
#     vins.add(line[0])
# print(vins)

master = []
for line in sys.stdin:
    line = line.split('\t')
    vin = line[0]
    val = line[1].split(",")
    if val[1]:
        print(vin, val[0], val[1], val[2].strip())


# [Logic to reset master info for every new group]
# Run for end of every group
def reset():
    pass


def flush():
    pass

# input comes from STDIN
# [parse the input we got from mapper and update the master info]
# [update more master info after the key change handling]
# [detect key changes]
# for line in sys.stdin:
#     line = line.strip()
#     key, val = line.split("\t")
#     if current_vin != vin:
#         if current_vin != None:
#             # write result to STDOUT
#             flush()
#         reset()
#         current_vin = vin
#     # do not forget to output the last group if needed!
#     flush()
