''' 
We create a list of 1000 integer numbers and we print the min 
as well as its position in the list
'''
import random as ra
#set list of number and positions
test_list,min_list = [],[]

#initialise list
for x in range(0,1000):
    test_list.append(ra.randint(0,1000))

#print minimum    
minimum=min(test_list)
print(f'The minimum value of list is {minimum}.')

#find positions

#First method

# for i in range(0,1000):
#     if test_list[i]==minimum:
#         min_list.append(i+1)
# print('Minimum is located in positions {}.'.format(min_list))

#second method

for i in test_list:
    if i == minimum:
        print("Minimum is in position {} ".format((test_list.index(i)+1)))
        test_list[test_list.index(i)]+=1    #change the list to count next min in index
