'''Since I have made a guessing game already ,I decided to create the reverse.
You start by asking a user to guess  number 
following the computer makes the optimum 'guess' 
each time the user answers if the guess was the same ,more or less 
compared to the users guess number'''

#Prompt user to guess
print('Guess an integer 0 - 100:')
input('Press ENTER to continue')

#Main program
counter,start,end =0,0,100
while True:
	guessTaken =start + (end-start)//2
	
	answer = input(f'Is {guessTaken} the number you guessed,\n(y)Yes \n(m)More than guess, \n(l)Less than guess :').upper()
	print(answer)

#Check if answer in range and proceed

	if answer not in ['Y','M','L']:
		print  ('Please select an option from the given.')
		continue
	else:
		counter+=1
		if answer=='Y':
			print (f"Computer guessed right in {counter} tries")
			break
		elif answer == 'L':
			start = guessTaken
		else:
			end = guessTaken

input('Press ENTER to exit')




