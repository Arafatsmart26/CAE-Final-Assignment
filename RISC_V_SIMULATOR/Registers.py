class Register:
    def __init__(self, contents = int(0)):
        self.contents=contents

    def setContents(self, contents):
        mask = (1 << 32) - 1
        self.contents = contents & mask

    def getContents(self):
        return self.contents

def Initialize():
    registers=[]
    for i in range(0,32):
        registers.append(Register(int(0)))
    registers[2].setContents(0x7ffffff0) # set init value for the stack pointer, 'sp'
    registers[3].setContents(0x10000000) # set init value for the global pointer, 'gp'
    return registers

