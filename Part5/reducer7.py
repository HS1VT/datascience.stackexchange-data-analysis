#!/usr/bin/env python

from operator import itemgetter
import sys

current_id = None
current_count = 0
id = None

for line in sys.stdin:
    line = line.strip()
    id, count = line.split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue


    if current_id == id:
        current_count += count
    else:
        if current_id:
            print ('{}\t{}'.format(current_id, current_count))
        current_count = count
        current_id = id

if current_id == id:
    print ('{}\t{}'.format(current_id, current_count))
