#!/usr/bin/env python

from __future__ import print_function, unicode_literals, with_statement

# TODO: use a try/except/finally in case the file doesn't exist, is protected, etc. and to guarantee file is closed
inputFile = open("show_version.txt")
fileContents = inputFile.read()
print(fileContents)
print("\n")
print("fileContents variable type is: " + str(type(fileContents)))
inputFile.close()

with open("show_version.txt") as inputFile:
	fileContents = inputFile.readlines()
	for line in fileContents:
		print(line, end='')
	print("fileContents variable type is: " + str(type(fileContents)))

