scale=2
def ADD(instruction, registers):
    rs1 = registers[int(instruction[12:17],scale)]
    print(rs1.getContents())
    rs2 = registers[int(instruction[7:12],scale)]
    rd=bin(int(rs1.getContents(),scale)+int(rs2.getContents(),scale))[2:]
    registers[int(instruction[20:25],scale)].setContents(rd)
    print(rd)
    return registers
def LUI(instruction, registers):
    registers[int(instruction[20:25],scale)].setContents(instruction[0:20])
def ADDI(instruction, registers):
    rs1 = registers[int(instruction[12:17],scale)]
    registers[int(instruction[20:25],scale)].setContents(bin(int(rs1.getContents(),scale) + int(instruction[0:12],scale))[2:])