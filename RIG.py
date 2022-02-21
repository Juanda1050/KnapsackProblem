from ctypes import cast
import random


# Main function for print the introduction for RIG and ask the user how many instances wants to generate
def main():
    print("This is the Random Instance Generator\n")
    k = int(input("How many instances you want to generate?: "))
    instanceGenerator(k)


# Instance Generator where the user input the amount of objects, min and max values/weights
def instanceGenerator(k):
    try:

        # Loop with the amount of instances to generate, asking all the inputs
        for fileNumber in range(k):
            n = getInput(prompt="Enter the amount of objects for instance No." + str(fileNumber + 1) + ": ",
                         cast=int,
                         condition=lambda x: x > 0,
                         errorMessage="The size of the instance must be greather than zero. Try again.")
            v_min = getInput(prompt="Enter the minimum value of the objects for instance No." + str(fileNumber + 1) + ": ",
                             cast=int,
                             condition=lambda x: x > 0,
                             errorMessage="The minimum value of the instance objects must be greather than zero. Try again.")
            v_max = getInput(prompt="Enter the maximum value of the objects for instance No." + str(fileNumber + 1) + ": ",
                             cast=int,
                             condition=lambda x: x > v_min,
                             errorMessage="The maximum value of the instance objects must be greather than minimum value. Try again.")
            w_min = getInput(prompt="Enter the minimum weight of the objects for instance No." + str(fileNumber + 1) + ": ",
                             cast=int,
                             condition=lambda x: x > 0,
                             errorMessage="The minimum weight of the instance objects must be greather than zero. Try again.")
            w_max = getInput(prompt="Enter the maximum weight of the objects for instance No." + str(fileNumber + 1) + ": ",
                             cast=int,
                             condition=lambda x: x > w_min,
                             errorMessage="The maximum weight of the instance objects must be greather than minimum weight. Try again.")
            W = int(((n * (w_max + w_min) / 2) * 0.3))

            # Method for create and write a txt file
            with open("instances/output_" + str(fileNumber + 1) + ".txt", "w+") as instance:
                instance.write(str(n) + " " + str(W) + "\n")

            # Loop for random numbers into the txt file
                for rnd in range(0, n):
                    v_file = random.randint(v_min, v_max + 1)
                    w_file = random.randint(w_min, w_max + 1)
                    instance.write(str(v_file) + " " + str(w_file) + "\n")

            # Close the txt file
                instance.close()

    # Exception if the txt file can't create
    except FileNotFoundError:
        print("The text file directory does not exist")


# Function for validate all the inputs in the RIG
def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Invalid input. Try again.")


# Run main function
if __name__ == '__main__':
    main()
