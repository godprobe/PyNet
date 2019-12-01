#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement
import os

# (optional) Use IPs that can be locally pinged

# Use a variable to define whether using Win or Lin/Mac
WINDOWS = False

base_cmd_linux = 'ping -c 2 '
base_cmd_windows = 'ping -n 2 '
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

# Construct 254-entry list of IPs
# ...base IP should be 10.10.100.0
# (or 10.10.100.)
# Use 'range'
# List should be all IP addresses from...
# 10.10.100.1
# ...to...
# 10.10.100.254
base_ip = '10.10.100.'
base_ip = '192.168.2.'
ips = []
for i in range(1, 255):
    ips.append(base_ip + str(i))

# Use 'enumerate' to print all of the IPs and
# their list index.
# Should look similar to...
# 0 ---> 10.10.100.1
# ...
# 4 ---> 10.10.100.5
for each in enumerate(ips):
    print(str(each[0]) + " ---> " + each[1])

# Slice a new list of ...100.3 to ...100.6
# Use a loop and 'os.system("ping -c 3 10.10.100.3")',
# ping all the IPs in the short list
# For Windows, 'os.system("ping -n 3 10.10.100.3")'
subset = ips[0:7]
for ip in subset:
    os.system(base_cmd + ip)
# :print(base_cmd + ip)
