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
    # instr = format(instruction, '32b')
    # print("instr: " + instr)
    # equiv = str(instructionAnd(instruction, 7, 0))
    # print("equiv: " + equiv)
    # rd = str(instructionAnd(instruction, 12, 7))
    # print("rd: " + rd)
    # immediate = str(instructionAnd(instruction, 32, 12))
    # print("immediate: " + immediate)
    # origImm = str(instruction & 0b11111111111111111111000000000000)
    # print("origImm: " + origImm)
    # binOrig = format(int(origImm), '32b')
    # print("binOrig: " + binOrig)

    rd = instructionAnd(instruction, 12, 7)
    imm = extractImmediate(instruction, 32, 12, "U") # 'LUI' is a U-type operation, so use "U"

    # print("extracted immedate: " + str(imm))
    # print("extracted immediate bits" + format(imm, 'b'))

    registers[rd].setContents(imm<<12)

#def AUIPC(instruction, registers):

#ARITHMATIC
def ADD(instruction, registers):
    rs1 = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2 = registers[instructionAnd(instruction, 25, 20)].getContents()
    # rd = 0

    rd = rs1 + rs2
    registers[instructionAnd(instruction, 12, 7)].setContents(rd)


def ADDI(instruction, registers):
    rs1 = registers[instructionAnd(instruction, 20, 15)].getContents()
    rd = registers[instructionAnd(instruction, 12, 7)].getContents()
    immBits = extractImmediate(instruction, 32, 20, "I") # 'ADDI' is an I-type operation, so use "I"

    rd = rs1 + immBits

    # print("rs1: " + str(instructionAnd(instruction, 20, 15)))
    # print("imm: " + str(extractImmediate(instruction, 32, 20, "I")))
    # print("rd: " + str(instructionAnd(instruction, 12, 7)))

    registers[instructionAnd(instruction, 12, 7)].setContents(rd)



def SLTI(instruction, registers):
    rs1 = registers[instructionAnd(instruction, 20, 15)].getContents()
    rd = registers[instructionAnd(instruction, 12, 7)].getContents()
    imm = extractImmediate(instruction, 32, 20, "I") # 'SLTI' is an I-type instruction, so use "I"

    rd = int(rs1 < imm)

    registers[instructionAnd(instruction, 12, 7)].setContents(rd)

#def SLTIU(instruction, registers):




#Helper function
def instructionAnd(instruction, upperBound, lowerBound, bit_width = 32):
    mask = (1 << bit_width) - 1
    instruction &= mask  # limit to 'bit_width' bits
    return (instruction & (2**upperBound-2**lowerBound))>>lowerBound

def extractImmediate(instruction, upperBound, lowerBound, binType, bit_width = 32):
    """
    Bounds for extraction are: [lowerBound, upperBound[, i.e. lowerBound-bit is included, while upperBound-bit is NOT included.
    binType:
    "U" = for upper immediate stuff, like 'LUI' and 'AUIPC'
    "I" = for signed immediates, including arithmetic-, load- and shift-operations, like 'addi', 'lw' and 'slli' (and also 'jalr', surprisingly)
    "S" = for store operations, like 'sw'
    "UJ" or "J" = for jump operations, like 'jal' (but NOT 'jalr')
    "SB" or "B" = for branch operations, like 'bne'
    The "R" format is not used here, since that format contains no immediates
    """
    mask = (1 << bit_width) - 1
    instruction &= mask  # limit to 'bit_width' bits
    binImm = bin((instruction & (2**upperBound-2**lowerBound))>>lowerBound)[2:]
    if len(binImm) < upperBound - lowerBound: # if binary value of the immediate is now shorter, then at least 1 leading '0' was removed:
        binImm = "0" + binImm # replace missing '0' to avoid issues with positive numbers being regarded as negative on accident

    # not all immediates are signed, so pick the right value to return:
    match binType:
        case "U":
            return int(binImm, 2) # used for operations with upper immediates, like 'lui' and 'auipc'
        case "I":
            return signedBinToInt(binImm) # used for signed immediates, including load- and shift-operations, like 'lw' or 'slli'
        case "S":
            print("PROBLEM: 'STORE'-instruction immediates not yet implemented! Defaulting to signed value!")
            return signedBinToInt(binImm) # used for store-operations, like 'sw'
        case "UJ":
            print("PROBLEM: 'JUMP'-instruction immediates not yet implemented! Defaulting to signed value (since jump instructions use signed immediates)!")
            return signedBinToInt(binImm) # used for jump-operations, like 'jal'
        case _:
            print("PROBLEM: 'BRANCH'-instruction immediates not yet implemented! Defaulting to signed value (since branch instructions use signed immediates)!")
            return signedBinToInt(binImm) # used for branch-operations, like 'bne'
            


# def signed_32Bit(integer):
#     return integer & (-1>>32)

# function from ChatGPT for converting regular ints to what they would be if Python had signed ints
def int32_toSigned(n: int) -> int:
    n &= 0xFFFFFFFF  # Keep only 32 bits
    if n & 0x80000000:
        return n - 0x100000000
    return n

# function from ChatGPT to convert signed bit string to its equivalent signed int value
# (e.g., the signed binary string, "11111110", would return "-2", while "011111110" would instead return "254")
def signedBinToInt(b: str) -> int:
    value = int(b, 2)           # convert bin → int (unsigned)
    bits = len(b)

    if value & (1 << (bits - 1)):   # if sign bit is set
        value -= 1 << bits         # subtract 2^bits

    return value

# ---- DOESN'T WORK RIGHT NOW, IT SEEMS ----
# def signed32(b: str) -> int:
#     value = int(b, 2)
#     if len(b) < 32:
#         # print("value: " + str(value))
#         value = int(sign_extend_to_32(b))
#         print("value: " + str(value))
#     if value & 0x80000000:
#         value -= 0x100000000
#     return value

# # function from ChatGPT to sign-extend a binary string to become 32 bits wide
# def sign_extend_to_32(b: str) -> str:
#     sign_bit = b[0]                     # first bit = sign bit
#     return sign_bit * (32 - len(b)) + b

# # function to pad a binary string with 'amount'-number of 0's
# # if input amount is less than 1 (i.e. no padding was needed after all), simply returns the input binary string
# def pad_0_left(b: str, amount: int) -> str:
#     if amount < 1:
#         return b
#     return "0" * amount + b