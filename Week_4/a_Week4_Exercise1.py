#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement

# Dictionary representation of a network device
# includes:
# ip_addr, vendor, password
device = {
    'ip_addr': '192.168.1.1',
    'vendor': 'cisco',
    'password': '12345'}

# Print the ip_addr
print(device.get('ip_addr'))

# If vendor is 'cisco', set platform to 'ios'
# If vendor is 'juniper', set platform to 'junos'
vendor = device.get('vendor')
if vendor == 'cisco':
    device['platform'] = 'ios'
if vendor == 'juniper':
    device['platform'] = 'junos'

# Create bgp_fields dict
# includes:
# bgp_as, peer_as, peer_ip
bgp_fields = {
    'bgp_as': 'one',
    'peer_as': 'two',
    'peer_ip': 'three'
    }

# Using .update(), add all bgp_fields key/values to network device
device.update(bgp_fields)

# Using for, print all the device keys
for item in device:
    print(item)

# Using a single for, print all the device key/value pairs
for item in device:
    print(item + ":\t " + device[item])
    # TODO print this in better-formatted columns
