x = 25

if x==25:
    print ("YES you Rigth")
else:
    print ("No you wrong")


age = 20

if (age <=4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print ("You are kid")
elif (age >= 12) and (age < 19):
    print ("You are teen")
else:
    print ("You are old")


print ("-------END-------")


all_cars=['crusler','dacia','bmw','KIA','vw','seat','skoda','lada','audi','fprd','Chevrolett']
german_cars = ['bmw', 'vw', 'audi']

if 'lada'in  all_cars:
    print ("yes LADA")
else:
    primt("LADA MOT")

for xxxx in all_cars:
    if xxxx in german_cars:
        print (xxxx + " IS German")
    else:
        print (xxxx + " NOT GERMAN ")