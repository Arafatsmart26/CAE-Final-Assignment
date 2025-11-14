from Interpreter import *
from Registers import *
j = 0
def Reader():
    size = 4 #Defines how many bytes we will read at a time. 
    instructions = [] #We initializa the array that will hold our instructions
    scale = 16 #This number is used to tell the int function that the number it parses is in base 16
    num_of_bits = 32 #The number of bits we would like each instruction to have, this is used to fill the empty places in the instruction up to 32

    with open('RISC_V_SIMULATOR/tests/task1/addlarge.bin', 'rb') as f:
        while True:
            chunk = f.read(size) #Each chunk is 4 bytes
            if not chunk: #This checks if the chunk is empty, if it is we break the while loop
                break
            chunk = chunk[::-1]
            instructions.append(int(chunk.hex(),scale)) #We convert the hexcode to binary, remove the prefix and fills in extra bits if needed
    # print("instr[0] (lui x10 524288) " + str(instructions[0]))
    # print("instr[1] (addi x10 x10 1) " + str(instructions[1]))
    # print("instr[2] (lui x11 524288) " + str(instructions[2]))
    # print("instr[3] (addi x11 x11 -2) " + str(instructions[3]))
    # instr0 = format(instructions[0], '032b')
    # instr1 = format(instructions[1], '032b')
    # instr2 = format(instructions[2], '032b')
    # instr3 = format(instructions[3], '032b')
    # print(instr0)
    # print(instr1)
    # print(instr2)
    # print(instr3)
    return instructions
# for i in Reader():
#     print(i)
for i in Reader():
    Interpreter(i)
for i in getRegisters():
    print("Register_" + str(j) + " " + hex(i.getContents()))
    j += 1
