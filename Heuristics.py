# Menu Function for print the menu of choices to solve the KP instance
import os
from pathlib import Path

def heuristicMenu():
    menu_log = """
        Knapsack problem Heuristic menu
        Choose which heuristic want to use to resolve the KP

        1. Heuristic (1)
        2. Heuristic (2)
        3. Heuristic (3)

        """
    print(menu_log)
    option = int(input("Option: "))
    instanceReader(option)


def instanceReader(option):

    dir_path_file = "instances/"
    dir_path = os.listdir(dir_path_file)

    # Loop to print all the instances available
    for file in range(len(dir_path)):
        print(dir_path[file])

    file_option = int(input("Which file would you like to open?: "))

    # This is the path where Python searches for instances
    path_to_file = "instances/output_" + str(file_option) + ".txt"
    path = Path(path_to_file)

    try:
        with open("instances/output_" + str(file_option) + ".txt") as instance:
            content = instance.read()
            print(content)
    except IOError:
        print(f'Can not access to {path_to_file}')
    finally:
        print("Terminating process")

    if path.is_file():
        print(f'The file {path_to_file} exist')
    else:
        print(f'The file {path_to_file} does not exist')
        heuristicMenu()

    if option == 1:
        heuristicOne()
    elif option == 2:
        heuristicTwo()
    elif option == 3:
        heuristicThree()
    else:
        print("Option does not exist")

def heuristicOne():
    print("Heuristic 1")
def heuristicTwo():
    print("Heuristic 2")
def heuristicThree():
    print("Heuristic 3")

if __name__ == '__main__':
    heuristicMenu()
