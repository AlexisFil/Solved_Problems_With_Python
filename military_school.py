'''
This program enters the physical traits of a candidate 
and calculates his ability to enter a greek military school 
using current and older data.'''

def validate_data(data_type,prompt):
	while True:
		data=input(prompt)
		if data_type == 'sex':
			if data =='1':
				data = 'Male'
				break
			elif data =='2':
				data='Female'
				break
			else:
				print('There is no such option!')

		elif data_type == 'height':
			try: 
				data =float(data)
				data = data/100
				if data >0 and data<3:
					break
				else:
					print("Height out of range , retry!")
			except:
				print("Wrong data input")
		else:
			try: 
				data=float(data)
				if data >0 and data<500:
					break
				else:
					print("Height out of range , retry!")
			except:
				print("Wrong data input")
	return data
def get_data():
	print("I would like to know some data about the candidate:") 
	sex =validate_data('sex',"Is the candidate \n(1)male or \n(2)female? \n>")
	height = validate_data('height',"Give me the candidate height in cm\n>")
	weight=validate_data('weight',"Give me the candidate's weight in kg.\n>")
	
	return sex,height,weight

def calculate_requirements(limit,height,weight):
	dms = weight/(height**2)
	admission=False
	admission_old=False
	
	#Calculate with limits
	if height>=limit[0] and dms>=limit[1] and dms<=limit[2]:
		admission=True
	if height>=limit[3]:
		admission_old=True
	return admission,admission_old,dms

def show_results(admission,admission_old):
	if admission:
		m=("The candidate can enter mailitairy school")
	elif admission_old:
		m=("The candidate cannot be accepted in militairy school though he/she could in the past.")
	else:
		m=('The candidate cannot enter military school.')
	return m
    
#Main  Program
#Set standards
#Min Height current
height_male=1.7
height_female=1.65

#DMS :Indicator of body mass
dms_male_min=20
dms_male_max=25
dms_female_min=16
dms_female_max=22

#old standards
height_male_old=1.65
height_female_old=1.55

#Main Loop
while True:
	#Exit
	exit_option = input("Press q to exit or any key to continue")
	if exit_option.upper()=='Q':
		break
	
	sex,height,weight = get_data()
	
	#Setting limits
	if sex == '1':
		limit=[height_male,dms_male_min,dms_male_max,height_male_old]
	else:
		limit=[height_female,dms_female_min,dms_female_max,height_female_old]
		
	admission,admission_old,dms = calculate_requirements(limit,height,weight)
	
	#Results
	message = show_results(admission,admission_old)
	print(f'''
###########################################################################
#	Test Results                                        
###########################################################################
Candidate Information:
Sex: {sex}Height: {height} -----  Requirement:{limit[0]} --Old Standard:{limit[3]}
Weight {weight}
DMS {dms} -----Requirement:{limit[1]} up to {limit[2]}                                               	
###########################################################################
#Verdict: {message}
###########################################################################
''')
