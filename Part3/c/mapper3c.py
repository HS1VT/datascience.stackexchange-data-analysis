#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

for line in sys.stdin:
    
    pattern = re.compile(r'CreationDate="(.{10})T(\d{2})(.{10})"\sScore')

    for match in pattern.finditer(line):
        hour = match.group(2)
        print("{}\t{}".format(hour, 1))

