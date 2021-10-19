#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

for line in sys.stdin:
    
    # to extract the month and comment from the line
    pattern = re.compile(r'\sText="(.*)"\sCreationDate="(\d{2})(\d{2})(-)(\d{2})(.{16})"\sUserId')

    for match in pattern.finditer(line):
        # month stores the month and the year
        month = match.group(3) + match.group(5)
        # comment comment_content splits comment based on space i.e length of comment_content is the number of words in the comment
        comment_content = match.group(1).split()
        comment_length = len(comment_content)

        # printing key, value pair for each month        
        print("{}\t{}".format(month, comment_length))
