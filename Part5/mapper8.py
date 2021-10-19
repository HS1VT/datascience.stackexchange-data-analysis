#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re
  

for line in sys.stdin:
    
    
    pattern = re.compile(r'row\sId="(.*)"\sReputation="(.*)"\sCreationDate')

    
    for match in pattern.finditer(line):
        row_ID = match.group(1)
        rep = match.group(2)
        print("{}\t{}".format(row_ID, rep))
