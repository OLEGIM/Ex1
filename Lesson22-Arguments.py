import sys
import os

x = len(sys.argv)
if x > 1:
    if sys.argv[1] =="/?":
        print("Help")
        print("Help2")
    print("Argumets entered: " + str(sys.argv[1:]))
else:
    print("not arg")

os.system('dir /D')