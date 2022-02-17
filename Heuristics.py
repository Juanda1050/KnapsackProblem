# Menu Function for print the menu of choices to solve the KP instance
import os
from pathlib import Path


def instanceReader():

    dir_path_file = "instances/"
    dir_path = os.listdir(dir_path_file)

    # Loop to print all the instances available
    for file in range(len(dir_path)):
        print(dir_path[file])

    file_option = int(input("Which file would you like to open?: "))

    # This is the path where Python searches for instances
    path_to_file = "instances/output_" + str(file_option) + ".txt"
    path = Path(path_to_file)

    if path.is_file():
        print(f'The file {path_to_file} exist')
    else:
        print(f'The file {path_to_file} does not exist')
        instanceReader()

    try:
        with open("instances/output_" + str(file_option) + ".txt") as instance:
            content = instance.read()
            print(content)
    except IOError:
        print(f'Can not access to {path_to_file}')

if __name__ == '__main__':
    instanceReader()
