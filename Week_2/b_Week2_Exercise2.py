#!/usr/bin/env python

from __future__ import print_function, unicode_literals

# Make a list of five IP addresses
IP_addresses = ['192.168.2.1','255.255.255.1','1.1.1.1','127.0.0.1','192.168.1.1']

# Use the .append() method to add an IP address onto the end
IP_addresses.append('42.11.38.123')

# Use the .extend() method to add two more to the end of the list
IP_addresses.extend(['1.2.3.4','5.6.7.8'])

# Print out the entire list of IP addresses
print("IP_addresses (all): " + str(IP_addresses))

# Print out the first IP address
print("First IP address: " + str(IP_addresses[0]))

# Print out the last IP address
print("Last IP address: " + str(IP_addresses[-1]))

# Using the .pop() method, remove the first address and the last
IP_addresses.pop(0)
IP_addresses.pop()
print("Popped first and last addresses: " + str(IP_addresses))

# Update the new first address in the list to be '`2.2.2.2`'
IP_addresses.insert(0,'2.2.2.2')

# Print out the new first address
print("2.2.2.2 added to the front; new first address from IP_addresses: " + str(IP_addresses[0]))
