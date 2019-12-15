#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement

# Create three lists of IP addresses
# 1) Houston data center routers, over ten RFC1918 IPs (some duplicates)
# 2) Atlanta data center routers, at least eight RFC1918 IPs (Houston overlap)
# 3) Chicago data center routers, at least eight, overlap Houston and Atlanta
IPs_Houston = [
    '123.123.123.123',
    '123.321.321.321',
    '123.213.213.213',
    '123.231.231.231',
    '123.312.312.312',
    '123.132.132.132',
    '123.123.123.123',
    '123.132.132.132',
    '123.100.0.1',
    '123.100.0.2',
    '123.100.0.3',
    '123.100.0.4',
    '123.100.0.5',
    '123.100.0.6',
    '123.100.0.7',
    '123.100.0.8',
    '123.100.0.9']

IPs_Atlanta = [
    '123.123.123.123',
    '123.321.321.321',
    '123.100.0.1',
    '123.100.0.2',
    '123.101.0.1',
    '123.101.0.1',
    '123.101.0.2',
    '123.101.0.2']

IPs_Chicago = [
    '123.321.321.321',
    '123.100.0.1',
    '123.100.0.2',
    '123.101.0.1',
    '123.101.0.1',
    '123.101.0.2',
    '123.102.1.1',
    '123.231.231.231',
    '123.312.312.312',
    '123.102.1.2']

# Convert each of the lists to a set
IPs_Hou = set(IPs_Houston)
IPs_Atl = set(IPs_Atlanta)
IPs_Chi = set(IPs_Chicago)

# Using a set operation, find...
# - Duplicates between Houston/Atlanta
IPs_HouAtl = []
for each in IPs_Hou:
    if each in IPs_Atl:
        IPs_HouAtl.append(each)
print(IPs_HouAtl)

# - Duplicates between all three sites
# - Unique IPs in Chicago
