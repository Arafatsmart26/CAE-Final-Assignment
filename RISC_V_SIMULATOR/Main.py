import glob
import os
from runCode import *
def Y_or_N():
    while True:
        print("Y or N?")
        user_input = input()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        print("It has to be either a Y or a N")

while True:
    print("Welcome to our RISC-V simulator")
    print("This program runs on python and takes a binary file of RISV-V instructions based on the RV32I base instruction set")
    print("The program runs on the path RISC_V_SIMULATOR\\tests")
    print("Do you wish to run a test?")
    answer = Y_or_N()
    if answer == True:
        print("Choose a task folder for the test please, it has to be a number between 1 and 4:")
        answer = input()
        if answer == "1" or answer == "2" or answer == "3" or answer == "4":
            base_path = os.path.join("RISC_V_SIMULATOR", "tests", "task" + str(answer), "*.bin")
        else: 
            print("That is not a number between 1 and 4")
            break
        print("Do you wish to choose a specific task?")
        answer = Y_or_N()
        if answer == True:
            print("Please write the name of the file you would like to run:")
            print("Printing task names:")
            for filename in glob.glob(base_path):
                print(f"{filename}")
            print("Write the name of the file you would like to be run, just write the name between the \\ and .bin")
            answer = "RISC_V_SIMULATOR\\tests\\task1\\" + input() +".bin"
            print("Running file: " + str(answer))
            run_code(answer)
        else: 
            print("Running all tasks")
            for filename in glob.glob(base_path):
                print(f"Reading file: {filename}")
                run_code(filename)
    else:
        print("Do you wish to end the program?")
        answer = Y_or_N()
        if answer == True:
            break


