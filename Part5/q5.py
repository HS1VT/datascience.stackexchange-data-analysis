import numpy as np
data_file = open('out_rep.txt')
data_file1 = open('out_UserId.txt')
data_rep = data_file.readlines()
data_user = data_file1.readlines()
for i in range(len(data_rep)) :
    data_rep[i] = list(map(int, data_rep[i].split()))
for j in range(len(data_user)):
    data_user[j] = list(map(int, data_user[j].split()))

rep=[]
noans=[]

for i in range(0,len(data_user)):
    for j in range(0,len(data_rep)):
        if data_user[i][0]==data_rep[j][0]:
            rep.append(data_rep[j][1])
            noans.append(data_user[i][1])

corr=np.corrcoef(rep,noans)
print('The correlation coefficient is:',corr[0][1])


