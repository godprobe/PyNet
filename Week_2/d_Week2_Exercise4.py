#!/usr/bin/env python

from __future__ import print_function, unicode_literals, with_statement

# Read in the "show\_ip\_int\_brief.txt" file into your program
# using the `.readlines()` method.
with open("show_ip_int_brief.txt") as ip_int_brief:
    interfaces = ip_int_brief.readlines()

# Obtain the list entry associated with the FastEthernet4 interface.
# You can just hard-code the index at this point since we haven't covered
# for-loops or regular expressions.
# Use the string `.split()` method to obtain both the IP address and
# the corresponding interface associated with the IP.
interface = ''
for item in interfaces:
    if "FastEthernet4" in item:
        interface = item

details = interface.split()

# Create a two element tuple from the result `(intf_name, ip_address)`.
# Print that tuple to the screen.
print((details[0], details[1]))

# Use `pycodestyle` on this script. Get the warnings/errors to zero.
# You might need to '`pip install pycodestyle`' on your computer
# (you should be able to type this from the shell prompt).
# Alternatively, you can type '`python -m pip install pycodestyle`'.
