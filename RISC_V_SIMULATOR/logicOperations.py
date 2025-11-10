def ADD(instruction, registers):
    scale=2
    registers[int(instruction[12:17],2)].setContents("00111")
    registers[int(instruction[7:12],2)].setContents("01000")
    rs1 = registers[int(instruction[12:17],2)]
    rs2 = registers[int(instruction[7:12],2)]
    rd=bin(int(rs1.getContents(),2)+int(rs2.getContents(),2))[2:]
    registers[int(instruction[20:25],2)] = rd
    print(rd)
    return registers