from Interpreter import *

class PC:
    def __init__(self, instructions = [], counter = 0):
        self.instructions = instructions
        self.counter = counter
        self.counter_max = len(instructions)
    def nextInstruction(self):
        self.counter +=1
    def jumpInstruction(self, instruction_index):
        self.counter = instruction_index
    
    def getInstructionCounter(self):
        return self.counter
    
    def setInstructionCounter(self, counter):
        self.counter = counter
    
    def addToProgramCounter(self, num):
        self.counter += num

    def getMaxInstruction(self):
        return len(self.instructions)