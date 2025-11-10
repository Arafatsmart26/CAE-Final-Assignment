class Register:
    def __init__(self, contents = "00000000"):
        self.contents=contents

    def setContents(self, contents):
        self.contents=contents
    def getContents(self):
        return self.contents
def Initialize():
    registers=[]
    for i in range(0,32):
        registers.append(Register("00000000"))
    return registers
print(len(Initialize()))
