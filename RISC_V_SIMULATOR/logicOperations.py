scale=2
def ADD(instruction, registers):
    rs1 = registers[int(instruction[12:17],scale)]
    rs2 = registers[int(instruction[7:12],scale)]

    rd=bin(int(rs1.getContents(),scale)+int(rs2.getContents(),scale))[2:]
    registers[int(instruction[20:25],scale)].setContents(rd)

def LUI(instruction, registers):
    registers[int(instruction[20:25],scale)].setContents(bin(int(instruction[0:20],2) << 12))

def ADDI(instruction, registers):
    rs1 = registers[int(instruction[12:17],scale)]
    rd = registers[int(instruction[20:25],scale)]

    rd.setContents(bin(int(rs1.getContents(),scale) + binToInt(instruction[0:12],scale))[2:])
    registers[int(instruction[20:25],scale)] = rd



#Helper function
def binToInt(binaryString, scale):
    value=int(binaryString, scale)
    if binaryString[0] == "1":
        value = value - 2**len(binaryString)
    print(value)
    return value
