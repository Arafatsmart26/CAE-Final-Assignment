import glob
import os
from runCode import *
#Please run this code, in the demo


def Y_or_N():
    while True:
        print("Y or N?")
        user_input = (input()).lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        print("It has to be either a Y or a N")

while True:
    print("Welcome to our RISC-V simulator")
    print("This program runs on python and takes a binary file of RISV-V instructions based on the RV32I base instruction set")
    print("The program runs in the folder 'RISC_V_SIMULATOR'")
    print("Do you wish to run a test?")
    answer = Y_or_N()
    if answer == True:
        dir_name = ""
        print("Choose a task folder for the test please, it has to be a number between 1 and 4:")
        task_folder = input()
        print("answer is: " + task_folder)
        if task_folder == "1" or task_folder == "2" or task_folder == "3" or task_folder == "4":
            dir_name = os.path.dirname(__file__)
            base_path = os.path.join(dir_name + "\\tests", "task" + str(task_folder), "*.bin")
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
            answer = os.path.join(dir_name + "\\tests", f"task{task_folder}", input() + ".bin" )
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


