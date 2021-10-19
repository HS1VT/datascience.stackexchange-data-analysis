#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    pattern = re.compile(r'ViewCount="(\d*)"(.*)Title="(.*)"\sTags')
    # split the line into words
 

    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for match in pattern.finditer(line):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        views = match.group(1)
        title = match.group(3)
      
        print("{}\t{}".format(views, title))
