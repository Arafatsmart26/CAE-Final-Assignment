
# Reader code, before returning the final list of instructions:
print("instr[0] (lui x10 524288) " + str(instructions[0]))
print("instr[2] (lui x11 524288) " + str(instructions[2]))
print("instr[3] (addi x11 x11 -2) " + str(instructions[3]))
instr0 = format(instructions[0], '32b')
instr2 = format(instructions[2], '32b')
instr3 = format(instructions[3], '32b')
print(instr0)
print(instr2)
print(instr3)
opcode0 = instructions[0] & 0b00000000000000000000000001111111
opcode2 = instructions[2] & 0b00000000000000000000000001111111
opcode3 = instructions[3] & 0b00000000000000000000000001111111
print(opcode0)
print(opcode2)
print(opcode3)


# LUI code
print("start of LUI")
rd = (instruction & 0b00000000000000000000111110000000) >> 7 # extract 'rd'
imm = (instruction & 0b11111111111111111111000000000000) >> 12 # extract immedate
print(instruction)
print(rd)
print(bin(imm))
print(str(rd))
print(binToInt(str(rd), scale))
print(str(imm))
registers[binToInt(str(rd), scale)].setContents(binToInt(str((imm) << 12), scale))
# print(hex(instruction & 2**12-2**7 >>7))
print("lolcat")