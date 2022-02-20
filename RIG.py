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
            n = int(input("Enter the amount of objects for instance No." + str(fileNumber + 1) + ": "))
            v_min = int(input("Enter the minimum value of the objects for instance No." + str(fileNumber + 1) + ": "))
            v_max = int(input("Enter the maximum value of the objects for instance No." + str(fileNumber + 1) + ": "))
            w_min = int(input("Enter the minimum weight of the objects for instance No." + str(fileNumber + 1) + ": "))
            w_max = int(input("Enter the maximum weight of the objects for instance No." + str(fileNumber + 1) + ": "))
            W = int(((n * (w_max + w_min) / 2) * 0.3))

            # Method for create and write a txt file
            with open("instances/output_" + str(fileNumber + 1) + ".txt", "w+") as instance:
                instance.write(str(n) + " " + str(W) + "\n")

            # Loop for random numbers into the txt file
                for rnd in range(1, n):
                    v_file = random.randint(v_min, v_max + 1)
                    w_file = random.randint(w_min, w_max + 1)
                    instance.write(str(v_file) + " " + str(w_file) + "\n")

            # Close the txt file
                instance.close()

    # Exception if the txt file can't create
    except FileNotFoundError:
        print("The text file directory does not exist")


# Function for validate all the inputs in the RIG
def getInput(prompt = "", cast = None, condition = None, errorMessage = None):
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
