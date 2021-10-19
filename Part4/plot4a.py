#!/usr/bin/env python
# importing numpy and matplotlib to plot graph

import numpy as np
import matplotlib.pyplot as plt

# opening file and storing all the lines as elements of list content
foo = open("Out.txt","r")

x = []
y = []

content = foo.readlines()

# for each line of sorted reducer output
for line in content:
    # split on basis of '(' present at start of value tuple
    # number of views stored in word and appended to x, count stores value tuple 
    word, count = line.split('(', 1)
    word = word.strip()
    # count split on basis of ','; median_length saves median length of comments made in the month, removing end characters ')]'
    #num_comments = count.split(',')[0]
    median_length = count.split(',')[1][1:-2]
    # month appended in the format mon'yr to x; median length appended to y
    x.append(word[0:3]+"'"+word[-2:])
    y.append(int(median_length))

# closing file
foo.close()

# plotting month on x axis, median length (acc. to no. of words) on y axis; plotting scatter and bar for better visualisation
plt.figure(1, figsize = (11,4))
plt.plot(x, y, color = 'b')
plt.scatter(x, y, color = 'b')
plt.bar(x, y, alpha = 0.3)

# axis customisation
axis_scale = 1
#plt.yticks(np.arange(min(y), max(y)+1, 1000))
plt.xticks(rotation = 90, ha = 'left')

# labels
plt.xlabel('MONTH')
plt.ylabel('MEDIAN LENGTH OF COMMENTS')
plt.title('COMMENT LENGTH MEDIAN DISTRIBUTION')

plt.show()
