'''
Tryout program
This program calculates if a candidate can aquire pension
in greek the value is stamps and the criteria are:
fullpension: age over 60 - stamps:over 4.500
lesspension: age over 50 or over 3000 stamps
modifiers :If number of kids > 4 stamps count 20% more
heavy duty job: count twice
'''
class candidate():
    '''A class for each pension candidate''' 
        def __init__(self,name,age,stamps,over4)
	self.name=name
	self.stamps=0
	self.age=age 
	self.over4=False
	self.pension=pension
 			
def calculate_stamps(job_stamps,heavy_duty,over4):
	if heavy_duty:
		job_stamps*=2
	if over4:
		job_stamps*=1.2
	return(job_stamps)


def calculate_pension(stamps,age):
	if age>=60 and stamps>=4500:
		message='Candidate able for pension'
	elif age>=50 and stamps>=4500:
		message='Candidate able for lesser pension'
	elif age>=60 and stamps>=3500:
		message='Candidate able for lesser pension'
	else:
		message='Candidate not able for pension'
	return message


def validate_data(data_type,prompt):
	while True:
		data=input(prompt)
		if data_type=='stamps':
			try: 
				data =float(data)
				if data >0 and data<100000:
					break
				else:
					print("Stamps out of range , retry!")
			except:
				print("Wrong data input")
		elif data_type=='age'
			try:
				data=int(data)
				if data>0 and data<200:
					break
				else:
					print("Age out of range , retry!")
		else:
			if data.upper == 'Y':
				data=True
				break
			elif data.upper == 'N':
				data=False
			else:
				print("Wrong data input!Please select one of the options.")

def get_data():
	pending_stamps=True:
	print("I would like to know some data about the candidate:") 
	firstname=input("Give me the candidate's first anme")
        surname= input("Give me the candidate's last name")
	name=firstname+' ' +lastname
        name=name+' '+surname
        age =validate_data('age',"What is the candidate's age? \n>")
	
	#Get the stamps from all jobs
	while pending_stamps:
		
	
	stamps= validate_data('height',"Give me the candidate height in cm\n>")
		weight=validate_data('weight',"Give me the candidate's weight in kg.\n>")
		status = 
		return name,sex,height,weight,status
	
				
				


	
	
