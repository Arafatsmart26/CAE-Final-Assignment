class Memory:
    def __init__(self, memory_address = 0x00000000, content = 0 ):
        self.memory_address = memory_address
        self.content = content
    def setMemoryAddress(self, memory_address):
        self.memory_address = memory_address
    def getMemoryAddress(self):
        return self.memory_address
    def setMemoryContent(self, content):
        self.content = content
    def getMemoryContent(self):
        return self.content
    def addMemory(self, memory_address, content):
        return Memory(memory_address,content)
    def addToMemoryContent(self,content):
        self.content += content