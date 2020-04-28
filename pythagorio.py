'''Θα χρησιμοποιήσουμε το πυθαγορείο θεώρημα:
A,B,Γ οι πλευρές ορθογωνίου τριγώνου
Δωθείσες A ,B υπολογίζουμε την υποτεινουσα Γ
όπου Α**2+Β**2=Γ**2


'''
#Συνάρτηση απόλυτης τιμής
def apolito(x):
    if x<0:
        x=x*(-1)
    return x

#Υπολογισμος ριζας
#To y είναι τυχαιος αριθμος κοντά στην ρίζα με προκαθορισμένο 1
def riza(x,y=1):
    
    def konta_stin_timi(x,y=1):
        if apolito(y**2-x)>0.001:
            return True
        else:
            return False

    def BeltioseRiza(x,y):
        return(((x/y)+y)/2)
        
        
   
    
    while konta_stin_timi(x,y):
        y= BeltioseRiza(x,y)

    return(y)
        





#Κυρίως πρόγραμμα
x =float((input("δώσε πλευρά Α τριγώνου:")))
y =float((input("δώσε πλευρά B τριγώνου:")))


print("η υποτείνουσα  είναι:{:.2f}".format(riza(x*x+y*y)))
    
