scale=2
#rs2 = registers[int(instruction[7:12],scale)]
#rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
#rd = registers[int(instruction[20:25],scale)]
#imm = binToInt(instruction[0:12],2)

#LOAD AND STORE
def LB(instruction, registers, memory):
    rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
    rd = registers[int(instruction[20:25],scale)]
    imm = binToInt(instruction[0:12],2)


#LOAD IMMEADIATE
def LUI(instruction, registers):
    registers[int(instruction[20:25],scale)].setContents(bin(int(instruction[0:20],2) << 12))
#def AUIPC(instruction, registers):

#ARITHMATIC
def ADD(instruction, registers):
    rs1 = registers[int(instruction[12:17],scale)]
    rs2 = registers[int(instruction[7:12],scale)]

    rd=bin(int(rs1.getContents(),scale)+int(rs2.getContents(),scale))[2:]
    registers[int(instruction[20:25],scale)].setContents(rd)


def ADDI(instruction, registers):
    rs1 = registers[int(instruction[12:17],scale)]
    rd = registers[int(instruction[20:25],scale)]

    rd.setContents(bin(int(rs1.getContents(),scale) + binToInt(instruction[0:12],scale))[2:])
    registers[int(instruction[20:25],scale)] = rd



def SLTI(instruction, registers):
    rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
    rd = registers[int(instruction[20:25],scale)]
    imm = binToInt(instruction[0:12],2)

    rd = bin(int(rs1<imm,2))[2:]

    registers[int(instruction[20:25],scale)] = rd

#def SLTIU(instruction, registers):




#Helper function
def binToInt(binaryString, scale):
    value=int(binaryString, scale)
    if binaryString[0] == "1":
        value = value - 2**len(binaryString)
    print(value)
    return value
