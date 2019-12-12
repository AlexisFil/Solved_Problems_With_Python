'''Program reads 500 integer numbers returns:
1.amount less than 11 
2.amount less than half the average
3.persentage of positive and negetive numbers of board'''

import random
test_list=[]

#enter 500 random numbers in test list
for i in range(0,500):
    test_list.append(random.randint(-20,100))

#Main program
print (test_list)    #The list is printed to check results

#A part

#a=[x for x in test_list if int(x) < 11]
#print(a)
print("There are {} numbers less than 11".format(len([x for x in test_list if int(x) < 11])))

#B part
half_average=(sum(test_list)/len(test_list))/2
#b=[x for x in test_list if int(x)<half_average]
print('There are {} numbers less than half the average'.format(len([x for x in test_list if int(x)<half_average])))

#C part
TotalPostives,TotalNegatives=0,0

for i in test_list:
    if i<0:
        TotalNegatives+=1
    else:
        TotalPostives+=1
print("The board is consisted of {:.2f}%  positives and {:.2f} negatives % ".format(TotalPostives/len(test_list)*100,TotalNegatives/len(test_list)*100))


