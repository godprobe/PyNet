#!/usr/bin/env python

from __future__ import print_function, unicode_literals, with_statement
from pprint import pprint

# Read in the "show\_arp.txt" file using the `readlines()` method. Use a *list slice* to remove the header line.
with open("show_arp.txt") as arpFile:
    arps = arpFile.readlines()[1:]
    # Use `pretty print` to print out the resulting list to the screen
    pprint(arps)
    # Create a new list slice that is only the first three ARP entries.
    threeArps = arps[0:3]
    # Use the `.join()` method to join these first three ARP entries back together as a single string
    # using the newline character ('`\n`') as the separator.
    arpString = '\n'.join(threeArps)
    # Write this string containing the three ARP entries out to a file named "arp_entries.txt".
    with open("arp_entries.txt",'w') as writeableFile:
        writeableFile.write(arpString)

