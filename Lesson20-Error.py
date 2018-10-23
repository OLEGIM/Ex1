import sys

filename = "lesson.txt"

while True:

    try:
        print("inside try")
        myfile = open(filename, mode='r', encoding='latin-1')
    except Exception:
        print ("Inside Except")
        print("Error Found")
        print(sys.exc_info()[1])
        filename = input ("input filename: ")
    else:
        print("inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print ("Inside Finally")

print ("===============EOF===============")