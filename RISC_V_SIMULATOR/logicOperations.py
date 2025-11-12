scale=2
#rs2 = registers[int(instruction[7:12],scale)]
#rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
#rd = registers[2**12-2**7]
#imm = binToInt(instruction[0:12],2)

#LOAD AND STORE
def LB(instruction, registers, memory):
    memoryCheck = 0
    size = 8

    rs1 = registers[instructionAnd(instruction,20, 15)].getContents()
    rd = registers[instructionAnd(instruction, 12, 7 )]
    imm = instructionAnd(instruction, 32, 20)

    address = (hex(rs1+imm))
    for i in memory:
        if address == i.getMemoryAddress():
            rd = i.getMemoryContent()[0:size]#Fix this
            memoryCheck = 1
            break
    if memoryCheck == 0:
        rd = 0x00
    
    registers[instructionAnd(instruction, 12, 7 )] = rd 

def LH(instruction, registers, memory):
    memoryCheck = 0
    size = 16

    rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
    rd = registers[int(instruction[20:25],scale)]
    imm = binToInt(instruction[0:12],scale)

    address = (hex(rs1+imm))
    for i in memory:
        if address == i.getMemoryAddress():
            rd = i.getMemoryContent()[0:size]
            memoryCheck = 1
            break
    if memoryCheck == 0:
        rd = 0x0000
    
    registers[int(instruction[20:25],scale)] = rd 

def LW(instruction, registers, memory):
    memoryCheck = 0
    size = 32

    rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
    rd = registers[int(instruction[20:25],scale)]
    imm = binToInt(instruction[0:12],scale)

    address = (hex(rs1+imm))
    for i in memory:
        if address == i.getMemoryAddress():
            rd = i.getMemoryContent()[0:size]
            memoryCheck = 1
            break
    if memoryCheck == 0:
        rd = 0x00000000
    
    registers[int(instruction[20:25],scale)] = rd 
#LOAD IMMEADIATE
def LUI(instruction, registers):
    registers[instructionAnd(instruction, 12, 7)].setContents(instructionAnd(instruction, 32, 12)<<12)
#def AUIPC(instruction, registers):

#ARITHMATIC
def ADD(instruction, registers):
    rs1 = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2 = registers[instructionAnd(instruction, 25, 20)].getContents()
    rd = 0

    rd = rs1 + rs2
    registers[instructionAnd(instruction, 12, 7 )].setContents(rd)


def ADDI(instruction, registers):
    rs1 = registers[instructionAnd(instruction,20, 15)].getContents()
    rd = registers[instructionAnd(instruction, 12, 7 )].getContents()
    print(rs1)
    print(type(rs1))
    print(instructionAnd(instruction, 32, 20))
    rd = rs1 + instructionAnd(instruction, 32, 20)
    registers[instructionAnd(instruction, 12, 7 )].setContents(rd)



def SLTI(instruction, registers):
    rs1 = registers[instructionAnd(instruction,20, 15)].getContents()
    rd = registers[instructionAnd(instruction, 12, 7 )].getContents()
    imm = instructionAnd(instruction, 32, 20)

    rd = int(rs1 < imm)

    registers[instructionAnd(instruction, 12, 7 )] = rd

#def SLTIU(instruction, registers):




#Helper function
def instructionAnd(instruction, upperBound, lowerBound, bit_width = 32):
    mask = (1 << bit_width) - 1
    instruction &= mask  # limit to 'bit_width' bits
    #print("This is instructionAnd" + str(-1 & instruction & 2**(upperBound)-2**(upperBound-1)))
    if instruction & (2**(upperBound)-2**(upperBound-1)) > 0:
        return ((instruction & (2**upperBound-2**lowerBound))>>lowerBound) & -2147483648


    return (instruction & (2**upperBound-2**lowerBound))>>lowerBound

def signed_32Bit(integer):
    return integer & (-1>>32)

