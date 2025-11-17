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
    return registers

