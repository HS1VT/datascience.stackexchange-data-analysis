import matplotlib.pyplot as plt
f=open('answer.txt',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split()[1])
f.close()
final=[]
for i in result:
    j=int(i)
    final.append(j)
final.sort()
x=[]
for k in range(0,648):
    x.append(k)

plt.plot(final,x)
plt.ylabel('Tags')
plt.xlabel('Number Of Times')
plt.title('Question 3(b)')
plt.show()
