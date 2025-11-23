from Program_Counter import *
from Reader import *
from Interpreter import *
from Registers import *

def run_code(filename):
    j = 0
    registers=Initialize() # reset register contents in case we're running multiple tests
    memory = [] # reset memory in case we're running multiple tests
    instructions = Reader(filename)
    program_counter = PC(instructions)

    while program_counter.getInstructionCounter() < program_counter.getMaxInstruction():
        counter = program_counter.getInstructionCounter()
        instruction = instructions[counter]
        Interpreter(instruction, registers, memory, program_counter)
        program_counter.nextInstruction()

    for i in registers:
        signed_reg_val = signedIntToHex(i.getContents(), 32) # convert the signed int in the register to two's-complement hex value
        print("Register_" + str(j) + " " + format(int(signed_reg_val, 16), '#010x')) # ugly print for printing 8 bytes in hex
        j += 1
    with open("output.res", "wb") as f:
        j = 0
        for i in registers:
            print("0x" + str(j) + " " + hex(i.getContents()))
            f.write(i.getContents().to_bytes(4, "little"))
            j += 1
            f.close
