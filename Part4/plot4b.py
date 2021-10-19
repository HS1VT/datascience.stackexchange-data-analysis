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
    # number of views stored in viewcount and appended to x, info stores value tuple 
    word, count = line.split('(', 1)
    word = word.strip()
    # count split on basis of ','; num_comments stores number of comments made in the month
    num_comments = count.split(',')[0]
    #median_length = count.split(',')[1][1:-2]
    # month appended in the format mon'yr to x; number of comments appended to y
    x.append(word[0:3]+"'"+word[-2:])
    y.append(int(num_comments))

# closing file
foo.close()

# plotting month on x axis, number of comments on y axis; plotting scatter and bar for better visualisation
plt.figure(1, figsize = (11,4))
plt.plot(x, y, color = 'b')
plt.scatter(x, y, color = 'b')
plt.bar(x, y, color = 'b', alpha = 0.3)

# axis customisation
axis_scale = 1
plt.xticks(rotation = 90, ha = 'left')
#plt.yticks(np.arange(min(y), max(y)+1, 1000))
plt.xticks(rotation = 90, ha = 'left')

# labels
plt.xlabel('MONTH')
plt.ylabel('NUMBER OF COMMENTS')
plt.title('COMMENT FREQ DISTRIBUTION')

plt.show()
