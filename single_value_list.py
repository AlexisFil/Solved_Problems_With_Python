myList = []
 #Main program
while True:
    choice = input('''Menu: \n-1.new entry \n-2. show \n-3.exit \nSelect >''')
    if choice !='1' and choice !='2' and choice != '3':                                               #Restart if not menu choice
                   print("Invalid choice please select a command from  menu\n")
                   continue
                
    if choice =='1':                                                                                  
        entry = input('Give me a new entry for list :')                               #With a try / except we can even filter the type of entry
        myList.append(entry)
        if myList.count(entry) ==2:                              #if two same entries remove the last
            myList.pop()

    elif choice =='2':                                                    #display list
        print(myList)

   else:                   
        break                                                        #exit program loop
