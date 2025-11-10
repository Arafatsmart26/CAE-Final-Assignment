def ADD(instruction, registers):
    scale=2
    rs1 = registers[int(instruction[12:17],2)]
    rs2 = registers[int(instruction[7:12],2)]
    rd=rs1+rs2
    registers[int(instruction[20:25],2)] = rd
    return registers