from __future__ import print_function, unicode_literals, division

with open("show_lldp_neighbors_detail.txt") as f:
    lines = f.readlines()
for line in lines:
    line = line.split(":")
    if "Port Did" in line[0] or "Systen"
