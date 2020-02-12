"""
A program challenging the user by taking two random numbers and asking him to calculate 
through pen and paper the various functions .
In version2 I will translate in greek.

"""
import random

def getnumbers():
    while True:
       a =  random.randint(1,100000)
       b = random.randint(1,100000)
       if abs(a-b)<500 or a<b or a<500 or b<500:
           continue
       else: break
    return(a,b)

def checkdecimals(a):
    b=int(a)
    if a == b:
        return(b)
    else:
        return(a)


def grading(x):
    if x == 0:
        grade = ['F',"You missed all four , how about relearning the basics?"]
    elif x == 1:
        grade = ['D',"You only found one . Need more work,I'm afraid."]
    elif x ==2:
        grade = ['C',"Found half the questions. If it was an exam you'd have barely passed!"]
    elif x == 3:
        grade = ['B',"Three out of four, so close!!!"]
    elif x == 4:
        grade = ['A',"Awesome all correct!!! Are you perhaps a computer yourself??"]
    else:
        grade = ['?',"Now how did you manage to get here?I am stunned!!"]
    return(grade)

         








#Main program
print('''######################################################################################################  
    Welcome to computer gymnastics the program where the user has to
calculate while the computer  makes the questions.I wait for you to take pen and 
paper before we start.
######################################################################################################\n
''')
correctAnswers = 0
prompt = ('> ')
input('Press Enter to start\n')

a,b = getnumbers()

print(f"First question {a} + {b} = ")
ans = input(prompt)
if int(ans) == a+b:
    print('Correct!\n')
    correctAnswers+=1
else:
    print(f'False! The correct answer is {a+b}\n')


a,b = getnumbers()


print(f"Second question {a} - {b} = ")
ans = input(prompt)
if int(ans) == a-b:
    print('Correct!\n')
    correctAnswers+=1
else:
    print(f'False! The correct answer is {a-b}\n')


a,b = getnumbers()

print(f"Third question {a} * {b} = ")
ans = input(prompt)
if int(ans) == a*b:
    print('Correct\n')
    correctAnswers+=1
else:
    print(f'The correct answer is {a*b}\n')


print(f"Fourth question {a} / {b} = ")
print(f'''Round the answer in 3rd decimal or lower:
        eg  2.78676 ===> 2.787
            3.00003 ===>3''')
ans = float(input(prompt))
correct = round(a/b,3)
correct = checkdecimals(correct)

if ans == correct:
    print('Correct!\n')
    correctAnswers+=1
else:
    print(f'False! The correct answer is {correct}\n')

grade = grading(correctAnswers)




print(f'''#######################################################
        \t\t GRADE   {grade[0]}
#######################################################

{grade[1]}
''')

input("Press ENTER to exit")
