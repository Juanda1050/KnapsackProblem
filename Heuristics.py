# Menu Function for print the menu of choices to solve the KP instance
import os
from pathlib import Path
import time

# Variable for clear console
clean_console = '\033[H\033[J'

# Function to print the Heuristics Menu 
def heuristicMenu(result, W):

    # Print to clean the command prompt
    print(clean_console, end='')

    # Variable to print the Heuristics Menu
    menu_log = """
        Knapsack problem Heuristic menu
        Choose which heuristic want to use to resolve the KP
        1. Heuristic (1)
        2. Heuristic (2)
        3. Heuristic (3)
        """
    print(menu_log)

    # Loop for validate that user puts a correct option
    while True:
        option = int(input("Option: "))
        if option == 1:
            heuristicOne(result, W)
            break
        elif option == 2:
            heuristicTwo(result, W)
            break
        elif option == 3:
            heuristicThree(result, W)
            break
        else:
            print("Option does not exist")
            continue

# Function for read the instance file selected by the user
def instanceReader():

    # Print to clean the command prompt
    print(clean_console, end='')

    # Variable to print the Instance Menu to use
    menu_log = """
            Knapsack problem Instance menu
            Choose which instance you will use
            """
    print(menu_log)

    # Variables to declare the route where are the output instances
    dir_path_file = "instances/"
    dir_path = os.listdir(dir_path_file)

    # Loop to print all the instances available
    for file in range(len(dir_path)):
        print(dir_path[file])

    # Loop to validate that instance exist
    while True:
        file_option = int(input("Which file would you like to open?: "))

        # This is the path where Python searches for instances
        path_to_file = "instances/output_" + str(file_option) + ".txt"
        path = Path(path_to_file)
        if path.is_file():
            print(f'The file {path_to_file} exist')
            break
        else:
            print(f'The file {path_to_file} does not exist')
            continue

    # Initialize array to store the data of output instance
    result = []

    # Reading the instance file option
    try:
        instance = open(path_to_file, 'r')
        first_line = instance.readline().split()
        W = int(first_line[1])
        for line in instance.readlines():
            result.append([int(x) for x in line.split(' ')])
    except IOError:
        print(f'Can not access to {path_to_file}')
    finally:
        print("Reading instance process conclude")

    # Call the heuristicMenu function
    heuristicMenu(result, W)


# Function for Heuristic One
def heuristicOne(result, W):
    print("Heuristic 1")

    # Variable for get the time take it of each heuristic
    solve_time_heuristic = time.time()

    # Sort the items before get into the loop to solve the heuristic
    result.sort(key=lambda x: -x[0])

    # Call function to get the objective function of heuristic one
    objectiveFuction(result, W, solve_time_heuristic)


# Function for Heuristic Two
def heuristicTwo(result, W):
    print("Heuristic 2")

    # Variable for get the time take it of each heuristic
    solve_time_heuristic = time.time()

    # Sort the items before get into the loop to solve the heuristic
    result.sort(key=lambda x: x[1])

    # Call function to get the objective function of heuristic one
    objectiveFuction(result, W, solve_time_heuristic)


# Function for Heuristic Three
def heuristicThree(result, W):
    print("Heuristic 3")

    # Variable for get the time take it of each heuristic
    solve_time_heuristic = time.time() 

    # Loop to obtain r
    for line in range(len(result)):
        v = result[line][0]
        w = result[line][1]
        result[line].append(v/w)

    # Sort the items before get into the loop to solve the heuristic
    result.sort(key=lambda x: -x[2])

    # Call function to get the objective function of heuristic one
    objectiveFuction(result, W, solve_time_heuristic)


# Function to solve the Heuristic and call it in every Heuristic function to get the objective function
def objectiveFuction(result, W, solve_time_heuristic):
    
    # Initialize variable to get the sum of values and sum of weights (objective function)
    sum_values = 0
    sum_weights = 0

    # Loop to store the items into the knapsack
    for i in range(len(result)):
        if sum_weights + result[i][1] <= W:
            sum_weights += result[i][1]
            sum_values += result[i][0]

    # Print the results of each heuristic
    print("Total of items: " + str(i + 1))
    print("Objective function: " + str(sum_values))
    print("Total weight in the knapsack: " + str(sum_weights))
    print("Residual: " + str(W - sum_weights))
    print("Execution time: " + str((time.time() - solve_time_heuristic)) + " s")


if __name__ == '__main__':
    instanceReader()
