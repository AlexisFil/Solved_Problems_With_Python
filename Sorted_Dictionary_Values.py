'''
A program typing  names and age info to a dictionary
The program sorts it by value and finally
prints the maximum and minimum values
'''

MaxAge,MinAge = -10,1000
MyDict = {}
while True:
	a = input ('give me a person\'s name for the list or press ENTER to stop :')
	if a =='':break
	b= int(input("Give me a person's age :"))
	MyDict[a]=b
	if b> MaxAge:MaxAge = b
	if b< MinAge:MinAge = b
print(MyDict)
li=sorted(MyDict.items(),key = lambda x:x[1],reverse = True)
print(li)
print(MaxAge,MinAge)
