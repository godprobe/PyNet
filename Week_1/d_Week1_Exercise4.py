#!/usr/bin/env python
from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip()

model = show_version.split()[1]
serial = show_version.split()[2]

print("Cisco model? " + str("Cisco".lower() in model.lower()))
print("Model 881? " + str("881" in model))

print("Model: \t" + model + "\t\tSerial: \t" + serial)

