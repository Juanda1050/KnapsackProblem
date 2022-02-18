# Menu Function for print the menu of choices to solve the KP instance
import os
from pathlib import Path
import time

start_time_program = time.time()


def heuristicMenu(result, W):
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


def instanceReader():
    menu_log = """
            Knapsack problem Instance menu
            Choose which instance you will use
            """
    print(menu_log)
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

    result = []

    try:
        instance = open(path_to_file, 'r')
        first_line = instance.readline().split()
        W = int(first_line[1])
        for line in instance.readlines():
            result.append([int(x) for x in line.split(' ')])
    except IOError:
        print(f'Can not access to {path_to_file}')
    finally:
        print("Reading process conclude")

    heuristicMenu(result, W)


def heuristicOne(result, W):
    print("Heuristic 1")
    result.sort(key=lambda x: -x[0])
    #print(result)

    sum_values = 0
    sum_weights = 0
    for i in range(len(result)):
        if sum_weights + result[i][1] <= W:
            sum_weights += result[i][1]
            sum_values += result[i][0]

    print("Objective function: " + str(sum_values))
    print("Total weight in the knapsack: " + str(sum_weights))
    print("Residual: " + str(W - sum_weights))
    print("Execution time: " + str(round(time.time() - start_time_program)) + "s")


def heuristicTwo(result, W):
    print("Heuristic 2")
    result.sort(key=lambda x: x[1])
    #print(result)

    sum_values = 0
    sum_weights = 0
    for i in range(len(result)):
        if sum_weights + result[i][1] <= W:
            sum_weights += result[i][1]
            sum_values += result[i][0]

    print("Objective function: " + str(sum_values))
    print("Total weight in the knapsack: " + str(sum_weights))
    print("Residual: " + str(W - sum_weights))
    print("Execution time: " + str(round(time.time() - start_time_program)) + "s")


def heuristicThree(result, W):
    print("Heuristic 3")

    for line in range(len(result)):
        v = result[line][0]
        w = result[line][1]
        result[line].append(v/w)

    result.sort(key=lambda x: -x[2])
    #print(result)

    sum_values = 0
    sum_weights = 0
    for i in range(len(result)):
        if sum_weights + result[i][1] <= W:
            sum_weights += result[i][1]
            sum_values += result[i][0]

    print("Objective function: " + str(sum_values))
    print("Total weight in the knapsack: " + str(sum_weights))
    print("Residual: " + str(W - sum_weights))
    print("Execution time: " + str(round(time.time() - start_time_program)) + "s")


if __name__ == '__main__':
    instanceReader()
