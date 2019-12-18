''' 
We create a list of 100 integer numbers and we print
the index of two max values in the list
'''
import random as ra
#set list of number
test_list,counter = [],0

#initialise list
for x in range(100):
    test_list.append(ra.randint(0,1000))

#find max   
maximum=max(test_list)
print(f'The maximum value of list is {maximum}.')

#print index of first 2 max values
while counter!= 2:
    for i in test_list:
        if i == maximum:
            print("Maximum found in index {} value :{}".format(test_list.index(i),maximum))
            counter +=1
            if counter==2:break
    maximum-=1


