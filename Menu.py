import os
import sys

menu = """
    Random Instance Generator / Heuristic solving
    Where do you want to start?
    
    1. Random Instance Generator
    2. Heuristic solving
    3. Exit
"""
print(menu)
while True:
    option = int(input("Option: "))
    if option == 1:
        os.system("python RIG.py")
        break
    elif option == 2:
        os.system("python Heuristics.py")
        break
    elif option == 3:
        sys.exit()
    else:
        print("Option does not exist")
        continue
