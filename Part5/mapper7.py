#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re
 
    

for line in sys.stdin:
    
    
    pattern = re.compile(r'PostHistoryTypeId="2"\s(.*)\sUserId="(\d*)"\s')

    
    for match in pattern.finditer(line):
        title = match.group(2)
    
        print("{}\t{}".format(title, 1))
