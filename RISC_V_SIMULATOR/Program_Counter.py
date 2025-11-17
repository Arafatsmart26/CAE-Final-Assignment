from Interpreter import *

class PC:
    def __init__(self, instructions = [], counter = 0):
        self.instructions = instructions
        self.counter = counter
        self.counter_max = len(instructions)
    def nextInstruction(self):
        if self.counter >= self.counter_max:
            return 
        self.counter +=1
        return self.instructions[self.counter]
    def jumpInstruction(self, instruction_index):
        self.counter = instruction_index
    
    def getInstructionIndex(self):
        return self.counter
    
    def setInstructionCounter(self, counter):
        self.counter = counter
