lista1=[]
while True :
#Για να μην προσθέτω συνέχεια χρησιμοποιώ δέικτη
    x=input("give TELOS to stop")
    if x=="TELOS":
        break

    element=input("give element of lista")

    if element not in lista1:
        lista1.append(element)
    print(lista1)
  
