

# Menu Function for print the menu of choices to solve the KP instance
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
    heuristicSwitch(option)


# Function for create a switch case option to choose the heuristic
def heuristicSwitch(option):
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
