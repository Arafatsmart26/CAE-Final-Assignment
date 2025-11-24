from Program_Counter import *
from Reader import *
from Interpreter import *
from Registers import *

def run_code(filename):
    j = 0
    registers=Initialize() # reset register contents in case we're running multiple tests
    memory = [] # reset memory in case we're running multiple tests
    instructions = Reader(filename) # read the instructions from the given binary file
    program_counter = PC(instructions) # initialize the program counter

    # run the code as long as the program counter is within the scope of the instructions
    while program_counter.getInstructionCounter() < program_counter.getMaxInstruction():
        counter = program_counter.getInstructionCounter() # check the program counter
        instruction = instructions[counter] # get the instruction we should run, based on the program counter
        Interpreter(instruction, registers, memory, program_counter) # interpret the instruction - this executes the instruction as well
        program_counter.nextInstruction() # increment the program counter so it's ready to fetch the next one in the next iteration

    # print all the registers to the terminal to make it easier to tell what's happening
    for i in registers:
        signed_reg_val = signedIntToHex(i.getContents(), 32) # convert the signed int in the register to two's-complement hex value
        print("Register_" + str(j) + " " + format(int(signed_reg_val, 16), '#010x')) # ugly print for printing 8 bytes in hex
        j += 1
    
    # create our 'output.res'-file, with data written as little endian (important!!)
    with open("output.res", "wb") as f:
        for i in registers:
            # in case of values overflowing in our registers on accident, take only the first 32 bits (sub-optimal, we know, but it works)
            f.write((i.getContents() & 0xFFFFFFFF).to_bytes(4, "little")) 