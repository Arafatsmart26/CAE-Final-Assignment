from Program_Counter import *
from Reader import *
from Interpreter import *
from Registers import *
import time

def run_code(filename):
    j = 0
    registers=Initialize() # reset register contents in case we're running multiple tests
    memory = [] # reset memory in case we're running multiple tests
    instructions = Reader(filename)
    # for i in instructions:
    #     print(format(i, '032b'))
    # exit()
    program_counter = PC(instructions)
    while program_counter.getInstructionCounter() < program_counter.getMaxInstruction():
        counter = program_counter.getInstructionCounter()
        instruction = instructions[counter]
        Interpreter(instruction, registers, memory, program_counter)
        # time.sleep(1)
        program_counter.nextInstruction()
    for i in registers:
        signed_reg_val = signedIntToHex(i.getContents(), 32) # convert the signed int in the register to two's-complement hex value
        print("Register_" + str(j) + " " + format(int(signed_reg_val, 16), '#010x')) # ugly print for printing 8 bytes in hex
        j += 1
