# Menu Function for print the menu of choices to solve the KP instance
import os


def menu():
    menu_log = """
    Knapsack problem Heuristic menu
    Choose which heuristic want to use to resolve the KP
    
    1. Heuristic (1)
    2. Heuristic (2)
    3. Heuristic (3)
    
    """
    print(menu_log)
    option = int(input("Option: "))
    return option


# Function for create a switch case option to choose the heuristic
def instanceReader(option):
    # This is the path where Python searches for instances
    path = "instances/"

    dir = os.listdir(path)

    # Loop to print all the instances available
    for file in range(len(dir)):
        print(dir[file])

    file_option = int(input("Which file would you like to open?: "))

    check = False

    if not check:
        check = os.path.isfile("instances/output_" + str(file_option) + ".txt")
        print(check)

    try:
        with open("instances/output_" + str(file_option) + ".txt") as instance:
            content = instance.read()
            print(content)
    except IOError:
        print("Can't access to the file")


def heuristicSwitcher(option):
    switcher = {
        1: heuristicOne,
        2: heuristicTwo,
        3: heuristicThree
    }
    # Get the function form switcher dictionary
    heuristic_option = switcher.get(option, "Invalid heuristic")

    # Execute the function
    return heuristic_option()


def heuristicOne():
    print("Heuristic 1")


def heuristicTwo():
    print("Heuristic 2")


def heuristicThree():
    print("Heuristic 3")


if __name__ == '__main__':
    menu()
