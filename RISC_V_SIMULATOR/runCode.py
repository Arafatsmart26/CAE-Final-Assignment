from Program_Counter import *
from Reader import *
from Interpreter import *
from Registers import *


def run_code(filename):
    j = 0
    instructions = Reader(filename)
    program_counter = PC(instructions)
    while program_counter.getInstructionCounter() < program_counter.getMaxInstruction():
        counter = program_counter.getInstructionCounter()
        instruction = instructions[counter]
        Interpreter(instruction)
        program_counter.nextInstruction()
    for i in getRegisters():
        print("Register_" + str(j) + " " + hex(i.getContents()))
        j += 1