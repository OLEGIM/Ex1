cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
print (cars)

for x in cars:
    print(x.upper())

for x in range(1,6):
    print(x)


mynumber_list = list(range(0, 10))
print(mynumber_list)

for x in mynumber_list:
    x= x*2
    print (x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print ("Max Numberis :" + str (max(mynumber_list)))
print ("Min Numberis :" + str (min(mynumber_list)))
print ("sum Numberis :" + str (sum(mynumber_list)))

cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[1:4]
print (mycars)
mycars = cars[:4]
print (mycars)

mycars = cars [-3:]
print(mycars)



cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[:]
print(cars)
print(mycars)
