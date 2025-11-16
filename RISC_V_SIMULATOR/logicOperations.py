scale=2
#rs2 = registers[int(instruction[7:12],scale)]
#rs1 = binToInt(registers[int(instruction[12:17],scale)].getContents(),2)
#rd = registers[2**12-2**7]
#imm = binToInt(instruction[0:12],2)

#LOAD AND STORE
def LB(instruction, registers, memory):
    size = 8 # number of bits to (attempt to) read from memory

    rs1_val = registers[instructionAnd(instruction,20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets
    mem_val = 0

    address = rs1_val + imm
    for i in memory:
        if address == i.getMemoryAddress():
            mem_val = i.getMemoryContent()[0:size]#Fix this
            break
    
    registers[instructionAnd(instruction, 12, 7 )].setContents(mem_val)

def LH(instruction, registers, memory):
    size = 16 # number of bits to (attempt to) read from memory

    rs1_val = registers[instructionAnd(instruction,20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets
    mem_val = 0

    address = rs1_val + imm
    for i in memory:
        if address == i.getMemoryAddress():
            mem_val = i.getMemoryContent()[0:size]#Fix this
            break
    
    registers[instructionAnd(instruction, 12, 7 )].setContents(mem_val)

def LW(instruction, registers, memory):
    # size = 32 # number of bits to (attempt to) read from memory - 32 bits means the entire 4-byte value in memory

    rs1_val = registers[instructionAnd(instruction,20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets
    mem_val = 0

    address = rs1_val + imm
    for i in memory:
        if address == i.getMemoryAddress():
            mem_val = i.getMemoryContent()
            break
    
    registers[instructionAnd(instruction, 12, 7 )].setContents(mem_val)

def SB(instruction, registers, memory):
    print("instruction: " + format(instruction, '032b'))
    print("rs1: " + format(instructionAnd(instruction, 20, 15), '05b'))
    print("rs2: " + format(instructionAnd(instruction, 25, 20), '05b'))

    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 10)].getContents()
    imm_upper = extractImmediate(instruction, 32, 25, "unsigned") << 5 # upper 7 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate

    print("rs1: " + str(rs1_val))
    print("rs2: " + str(rs2_val))
    print("imm_upper_bits: " + bin(imm_upper >> 5))
    print("imm_lower_bits: " + bin(rs1_val))


def SH(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 10)].getContents()

def SW(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 10)].getContents()


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

    # rd = instructionAnd(instruction, 12, 7)
    imm = extractImmediate(instruction, 32, 12, "unsigned")

    # print("extracted immedate: " + str(imm))
    # print("extracted immediate bits" + format(imm, 'b'))

    registers[instructionAnd(instruction, 12, 7)].setContents(imm<<12)

#def AUIPC(instruction, registers):

#ARITHMATIC
def ADD(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val + rs2_val)

def SUB(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val - rs2_val)


def ADDI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val + imm)


def SLL(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val << rs2_val)

def SLT(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    if rs1_val < rs2_val:
        registers[instructionAnd(instruction, 12, 7)].setContents(1)
    else: 
        registers[instructionAnd(instruction, 12, 7)].setContents(0)
    
def SLTU(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    if rs1_val < 0 :
        rs1_val = rs1_val + (1<<rs1_val.bit_length())
    if rs2_val < 0 :
        rs2_val = rs2_val + (1<<rs2_val.bit_length())

    if rs1_val < rs2_val:
        registers[instructionAnd(instruction, 12, 7)].setContents(1)
    else: 
        registers[instructionAnd(instruction, 12, 7)].setContents(0)

def SLTI(instruction, registers):
    rs1 = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(int(rs1 < imm))

#def SLTIU(instruction, registers):




#Helper function
def instructionAnd(instruction, upperBound, lowerBound, bit_width = 32) -> int:
    mask = (1 << bit_width) - 1
    instruction &= mask  # limit to 'bit_width' bits
    return (instruction & (2**upperBound-2**lowerBound))>>lowerBound

def extractImmediate(instruction, upperBound, lowerBound, immSign: str, bit_width = 32) -> int:
    """
    Bounds for extraction are: [lowerBound, upperBound[, i.e. lowerBound-bit is included, while upperBound-bit is NOT included.
    binType:
    "signed" = the immediate should be handled as a signed immediate
    "unsigned" = the immediate should be handled as an unsigned immediate
    """
    mask = (1 << bit_width) - 1
    instruction &= mask  # limit to 'bit_width' bits
    binImm = bin((instruction & (2**upperBound-2**lowerBound))>>lowerBound)[2:]
    if len(binImm) < upperBound - lowerBound: # if binary value of the immediate is now shorter, then at least 1 leading '0' was removed:
        binImm = "0" + binImm # replace missing '0' to avoid issues with positive numbers being regarded as negative on accident

    # not all immediates are signed, so return the appropriately interpreted value:
    match immSign.lower():
        case "signed":
            return signedBinToInt(binImm)
        case "unsigned":
            return int(binImm, 2)
            


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