#!/usr/bin/env python
from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac_entries = [mac1, mac2, mac3]

print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print(20*"-" + " " + 20*"-")
for entry in mac_entries:
	print("{:>20}{:>20}".format(entry.split()[1],entry.split()[3]))

