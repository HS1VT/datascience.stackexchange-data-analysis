The correlation coefficient is: 0.8361786264557619
This is the correlation between the number of answers by a user and his/her reputation.

EXPLAINATION OF THE CODE

the mapper7.py finds using regex the parts where we get PostHistoryTypeId=2, and whenever we get it, it prints the value userId,1. Now the Reducer7.py arranges this and gives this data in the form of UserId,Total_No_Of_Answers, we store this in a text file out_UserId.txt.

Now the mapper8.py traverses the Users.xml and collects all the data and prints it in the form of RowId,Reputation and we store this data in the form of out_rep.txt.

Finally we run the q5.py which takes input as both files: out_UserId and out_rep. It matches data from both the files and wherever the RowId from out_rep is equal to the UserId from out_UserId, it stores the repuation and No_of_answers by that user in the corresponding elements of two separate lists.

Now we use numpy and pass both the data in numpy.corrcoef(list1,list2) and we get the Correlation Coefficient as 0.8361786264557619


