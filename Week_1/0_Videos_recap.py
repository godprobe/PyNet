#!/usr/bin/env python
from __future__ import print_function
'''
#!/usr/bin/env python
Depending on environemnt (Mac/Linux) generally need 'shebang line' to execute py files
Also may need to chmod 755 file.py
Allows running file.py directly, e.g. ./file.py
'''

'''
from __future__ import print_function
	allows Python2 to use print("whatever"), like Python3, instead of print "whatever"

from __future__ import unicode_literals
	allows Python2 to use Python3 unicode strings without needing u'my_string'
	Python3 can force ASCII bytecode strings with b'my_string'
'''
# IPython (interactive Python shell) installed with: python -m pip install ipython

try: # Attempt raw_input for python2 compatability
	ip_addr = raw_input("Enter an IP address: ")
except NameError: # Python3 returns a NameError when attempting raw_input()
	ip_addr = input("Enter an IP address: ")

print(ip_addr)
print('192.168' in ip_addr)
print(ip_addr[0] + ' is the first char in the string, and the last char is '
		+ ip_addr[-1])

print("Binary: " + bin(int(ip_addr.split('.')[0])) +
	", Hex: " + hex(int(ip_addr.split('.')[0])) +
	", Int: " + str(int(ip_addr.split('.')[0])))

print(hex(int(ip_addr.split('.')[0])))

print("\testi\ng")
# versus
print(r"\testi\ng")

print('''this
	is
	a
	test.''')
# versus
print(repr('''this
	is
	a
	test.'''))

print('		\t\tstriptest   \n\n\n'.strip())
# split() with no params splits on whitespace, splitlines() splits on newlines

# dir(object) returns a list of attributes and methods available to that object
# help(obj.attr) / help(obj.method) shows a help page for that attr or method
# id(obj) reveals memory reference for obj; gc'd when all references lost
# type(obj) reveals the object type; Py2/3 have different return for strings

ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'
octets = ip_addr3.split('.')
print("\n")
print("-" * 80)

# formatting with 20-width columns, aligned right
print("{:>20}{:>20}{:>20}".format(ip_addr1, ip_addr2, ip_addr3))

# right/center/left aligned, using named arguments
print("{first:>20}{spam:^20}{foobar:<20}".format(foobar=ip_addr1, first=ip_addr2, spam=ip_addr3))

# 10-width columns, default alignment (left < ); center alignment is ^
print("{:10}{:10}{:10}{:10}".format(octets[0], octets[1], octets[2], octets[3]))

# print the items in a list more easily (same as above)
print("{:10}{:10}{:10}{:10}".format(*octets))

# printing using the older formatting style (just be aware of it)
print("%s %s" % (ip_addr1, ip_addr3))

# Python 3.6+: printing with var directly in the string, using f-strings
port1 = 8080
try:
	print(f"My IP address is: {ip_addr1:^20} {port1:^8}")
except:
	print()

print("-" * 80)
print("\n")
