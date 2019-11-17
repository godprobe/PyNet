#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement

# Read in show_ip_bgm_summ.txt file
# Obtain first and last lines of the output
with open("show_ip_bgp_summ.txt") as theFile:
    fileContents = theFile.readlines()
    firstLine = fileContents[0]
    lastLine = fileContents[-1]

# .split() first line to obtain AS number
ASNumber = firstLine.split()[-1]
# .split() last line to obtain IP address
IPAddress = lastLine.split()[0]

# Print both local AS number and the BGP peer IP address to the screen
print("Local AS number: " + ASNumber + " \tIP address: " + IPAddress)
