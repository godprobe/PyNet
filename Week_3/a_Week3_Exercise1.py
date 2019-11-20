#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement
from pprint import pprint

vlans = []
with open("show_vlan.txt") as theFile:
    fileContents = theFile.readlines()[2:]
    for line in fileContents:
        # Either the input is formatted strangely, or a test as follows is probably required
        try:
            int(line.split()[0])
            vlans.append((line.split()[0], line.split()[1]))
        except ValueError:
            continue
pprint(vlans)
