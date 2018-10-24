


enemy = {

    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudi',

}
print (enemy)

print ("Locatoon  X = " + str(enemy['loc_x']))
print ("Locatoon  Y = " + str(enemy['loc_y']))
print ("HIS name is  " + enemy['name'])

enemy ['rank'] = 'Admirak'
print (enemy)


del enemy['rank']
print (enemy)


enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] -30
if enemy ['health'] < 80:
    enemy['color'] = 'yellow'

print (enemy)

print(enemy.keys())
print(enemy.values())