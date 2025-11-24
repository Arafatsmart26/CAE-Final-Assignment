class Register:
    def __init__(self, contents = int(0)):
        self.contents=contents

    def setContents(self, contents):
        self.contents = contents

    def getContents(self):
        return self.contents

# this function initializes all our registers
# this also means our register list contains the registers in the correct order (x0-x31)
def Initialize():
    registers=[]
    for i in range(0,32):
        registers.append(Register(int(0)))
    return registers

