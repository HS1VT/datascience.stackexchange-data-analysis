#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
titles = []

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word, title = line.split('\t')
    # convert count (currently a string) to int
    #try:
        #count = int(count)
    #except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        #continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += 1
        titles.append(title)
    else:
        if current_word:
            # write result to STDOUT
            print ('{}\t({}, {})'.format(current_word, current_count, titles))
        titles[:] = []
        current_count = 1
        current_word = word
        titles.append(title)

# do not forget to output the last word if needed!
if current_word == word:
    print ('{}\t({}, {})'.format(current_word, current_count, titles))

