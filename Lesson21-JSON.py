
import json

filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')
player1 = {
    'PlayerName': "Donald TR",
    'Score': 345,
    'Awards': ["OR","NV","NY"]

}

player2 = {
    'PlayerName': "Vladimir",
    'Score': 346,
    'Awards': ["MSK", "SPB", "EKB"]

}

myplayers=[]
myplayers.append(player1)
myplayers.append(player2)

#========SAVE of JSON================


json.dump(myplayers, myfile)
myfile.close()


#========================LOAD JSON

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award №1 is: " + str(user['Awards'][0]))
    print("Player Award №2 is: " + str(user['Awards'][1]))
    print("Player Award №3 is: " + str(user['Awards'][2]))
    print("===================================\n\n")