#!/usr/bin/env python

from operator import itemgetter
import sys

# defining median function to call later and calculate median
# after sorting list of discrete elements:
# if len even, median = mean of middle elements
# if len odd, median = middle element 
def median(l):
    l.sort()
    if len(l)%2 == 0:
        median = (l[int(len(l)/2)] + l[int(len(l)/2 - 1)])/2
    else:
        median = l[int((len(l) - 1)/2)]

    return median

# for ease of interpretting output
no_month = {'01' : 'January', '02' : 'February', '03' : 'March', '04' : 'April', '05' : 'May', '06' : 'June', '07' : 'July', '08' : 'August', '09' : 'September', '10' : 'October', '11' : 'November', '12' : 'December'}

current_month = None
current_count = 0
month = None
lengths = []

for line in sys.stdin:
    line = line.strip()
    # storing key in month and length of the comment in length by sorting on basis of tab provided in mapper output
    month, length = line.split('\t', 1)
    
    # convert count to int; in case of error, drop the line
    try:
        length = int(length)
    except ValueError:
        continue

    # # if switch works only because Hadoop sorts mapper output before sending to reducer
    if current_month == month:
        # in this case, the key is same as previous one, therefore, current_count increased by one, length of comment appended to lengths
        current_count += 1
        lengths.append(length)
    else:
        # all the key value pair inputs for this key have been utilized 
        # therefore current_count = no. of times the key appears.
        # list lengths contains the lengths of all the comments made in the given month 
        if current_month:
            med = median(lengths)
            # key value pair printed as output from reducer
            # key is the value corresponding to month number in the no_month dictionary along with the year
            # value is a tuple containing first the number of comments in the month and then the median length of all these comments
            print ('{}\t({}, {})'.format(no_month[current_month[2:]]+', 20'+month[0:2], current_count, med))
        # list lengths emptied
        lengths[:] = []
        # to initiate process for the next key (the key that came in present iteration of the for loop)
        current_count = 1
        current_month = month
        # length of comment appended to the now emptied list lengths
        lengths.append(length)


# to print the the last key value pair to output
if current_month == month:
    med = median(lengths)
    print ('{}\t({}, {})'.format(no_month[current_month[2:]]+'+ 20'+month[0:2], current_count, med))
