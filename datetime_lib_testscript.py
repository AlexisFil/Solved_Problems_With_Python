"""
A simple code demonstrating the use of datetime library
for calendar dates manipulation
"""
from datetime import datetime,timedelta

#Current date
currentDate = datetime.now()

print("Today the date is \n> {}\n".format(currentDate))

#Print date in past/future

aWeek = timedelta(days=7)
aWeekAgo = (currentDate - aWeek)
print("A week ago  it was \n> {}\n".format(aWeekAgo))

#Specific information on a date 
#There is also selection for hours,minutes,seconds

print(f'''A week ago was:
Day:{aWeekAgo.day}
Month:{aWeekAgo.month}
Year:{aWeekAgo.year}
''')

#Input a date
birthday = input("When were you born?(Day/Month/Year)\n>")
birthDate=datetime.strptime(birthday,'%d/%m/%Y')

print(f'''\n+++++Birthday+++++
Day :{birthDate.day}
Month :{birthDate.month}
''')
age = currentDate - birthDate

print(f'You are:\n{age.days} days old!')



