




def napeshatat_privestvie(name):
    """PRIV"""

    print(" CONGRAT " + name + " best ")

def summa(x,y):
   return x + y

def factorial(x):
    """CALC FACTORIAL"""
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet *i
    return otvet

napeshatat_privestvie("DENIS")
napeshatat_privestvie("OLEG")

#x = summa(33, 22)
#print(x)


for i in range(1,10):
    print(str(i) + "!\t = " + str(factorial(i)))

print (factorial(1))
print (factorial(2))
print (factorial(5))
print (factorial(10))



