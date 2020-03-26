import pandas as pd
print("""##############################################################################
              File Converter
       Turn a csv file to excel and reverse with python
         ( Requires Pandas and xlwt  python modules )
###############################################################################""")
while True:
	choice = input('Press 1 for csv or 2 for excel file input \n >')
	if choice =='1' or choice == '2':
		break

while True:
	try:
		print('Give me file name (no ending):') 
		name = input('>')
		if choice == '1':
			file_name = name+'.csv'
			df = pd.read_csv(file_name)
			df.to_excel(name+'.xls')
			break
		else:
			file_name = name+'.xls'
			df = pd.read_excel(file_name)
			df.to_csv(name+'.csv')
			break
	except:
		print('File '+file_name+' not existing')
		choice2=input('Press X to exit  or ENTER to change name\n>')
		if choice2.upper() == 'X':
				break
        

