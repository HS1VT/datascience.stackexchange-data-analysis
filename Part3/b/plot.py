import numpy as np
import matplotlib.pyplot as plt

foo = open("Out_sorted.txt","r")

x = []
y = []

content = foo.readlines()

for line in content:
    viewcount, info = line.split('(', 1)
    freq = info.split(', [')
    x.append(int(viewcount))
    y.append(int(freq[0]))


foo.close()


plt.plot(x, y)
plt.xlabel('VIEWCOUNT')
plt.xticks(np.arange(1, max(x)+1, 20000))
plt.yticks(np.arange(1, max(y)+1, 20))
plt.ylabel('FREQ')
plt.title('VIEWCOUNT DISTRIBUTION')
plt.show()
