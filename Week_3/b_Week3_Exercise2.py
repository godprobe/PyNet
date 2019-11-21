#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement

with open("show_arp.txt") as theFile:
    arps = theFile.readlines()
    arps = arps[1:]
    isFoundDefault = False
    isFoundArista3 = False
    for line in arps:
        ip_addr = line.split()[1]
        mac_addr = line.split()[3]
        if ip_addr == '10.220.88.1':
            print("Default gateway IP/Mac" + "\t " + ip_addr + "/" + mac_addr)
            isFoundDefault = True
        if ip_addr == '10.220.88.30':
            print("Arista3 IP/Mac is" + "\t " + ip_addr + "/" + mac_addr)
            isFoundArista3 = True
        if isFoundDefault and isFoundArista3:
            # print("Found both, breaking out!")
            break
        # print("The search continues...")
