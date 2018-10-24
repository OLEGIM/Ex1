import re

input_filename = "../dumpfile.txt"
result_filename = "../results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')

mytext = inputfile.read()
lookfor = r"[\w.-]+@(?!sed\.org)[\w.-]+\.[\w.]+"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")


print ("Total: " + str(len(results)))

#inputfile.close()
#resultfile.close()