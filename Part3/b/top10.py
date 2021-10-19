#!/usr/bin/env python

from operator import itemgetter
import sys

top10 = []


for line in sys.stdin:
    line = line.strip()
    viewcount, info = line.split('\t(', 1)
    viewcount = int(viewcount.strip())
    freq, titles = info.split(', [', 1)
    titles = eval('['+titles[:-1])

    tuple_made = (viewcount, titles)

    if len(top10) == 0:
        top10.append(tuple_made)
    
    elif len(top10) < 10:
        top10.append(tuple_made)
        for i in range(len(top10)):
            if viewcount < top10[i][0]:
                top10.insert(i, tuple_made)
                top10[0:len(top10)] = top10[0:(len(top10)-1)]
                break
            
    else:
        for i in range(10):
            if viewcount > top10[(9 - i)][0]:
                top10.insert(10 - i, tuple_made)
                top10_new = top10[1:11]
                top10 = top10_new
                break 

for ele in top10:
    print(str(ele[0])+'      '+str(ele[1]))