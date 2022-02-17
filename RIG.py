import random

def main():
    print("This is the Random Instance Generator\n")
    k = int(input("How many instances you want to generate?: "))
    instanceGenerator(k)


def instanceGenerator(k):
    try:
        for fileNumber in range(k):
            n = int(input("Enter the amount of objects for instance No." + str(fileNumber + 1) + ": "))
            v_min = int(input("Enter the minimum value of the objects for instance No." + str(fileNumber + 1) + ": "))
            v_max = int(input("Enter the maximum value of the objects for instance No." + str(fileNumber + 1) + ": "))
            w_min = int(input("Enter the minimum weight of the objects for instance No." + str(fileNumber + 1) + ": "))
            w_max = int(input("Enter the maximum weight of the objects for instance No." + str(fileNumber + 1) + ": "))
            W = ((n * (w_max + w_min) / 2) * 0.3)

            with open("instances/output_" + str(fileNumber + 1) + ".txt", "w+") as instance:
                instance.write(str(n) + " " + str(W) + "\n")

                for rnd in range(1, n):
                    v_file = random.randint(v_min, v_max + 1)
                    w_file = random.randint(w_min, w_max + 1)
                    instance.write(str(v_file) + " " + str(w_file) + "\n")

                instance.close()
    except FileNotFoundError:
        print("The text file directory does not exist")

if __name__ == '__main__':
    main()
