#!/usr/bin/env python
from __future__ import print_function, unicode_literals

user_IP = ""
try:
	user_IP = raw_input("Please enter an IP address: ")
except NameError:
	user_IP = input("Please enter an IP address: ")
	octets = user_IP.split('.')

print("{:^15}{:^15}{:^15}{:^15}".format("Octet 1", "Octet 2", "Octet 3", "Octet 4"))
print(4*15*"-")
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print(4*15*"-")
