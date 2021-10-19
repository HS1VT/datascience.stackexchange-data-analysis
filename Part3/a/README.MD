All the names of tags and how many times they are used is stored in answer.txt
Then we run answer.py which is a python program which plots our data
Now, the distribution we get is stored in Plot.png
From observing the distribution, we get to know that the the distribution is Weibull Cumulative Distribution

EXPLAINATION OF CODE

In the mapper part, first we remove the leading and trailing whitespaces and then using re.compile we collect the names of all the tags and then output the result in the form of (tag,1).

Now in the reducer part, we see that wherever the same tag is repeated, it's count is increased by one. So at the end of the program we get the ouput in the form of (tag, no. of times it appeared)

