#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement

with open("show_lldp_neighbors_detail.txt") as theFile:
    lldps = theFile.readlines()
    portID = systemName = False
    for line in lldps:
        if "System Name" in line:
            systemName = line.split(':')[1]
        if "Port id" in line:
            portID = line.split(':')[1]
        if systemName and portID:
            break
print("System name is: " + systemName.strip() + ", and port ID is: " + portID.strip())
