from Memories import *
scale=2

#LOAD AND STORE
def LB(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets

    loaded_value = memLoad(memory, (rs1_val + imm), 1)
    signed_ext_value = int(sign_extend_to_32(bin(loaded_value)[2:]), 2)
    
    registers[instructionAnd(instruction, 12, 7)].setContents(signed_ext_value)

def LH(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets

    loaded_value = memLoad(memory, (rs1_val + imm), 2)
    signed_ext_value = int(sign_extend_to_32(bin(loaded_value)[2:]), 2)
    
    registers[instructionAnd(instruction, 12, 7)].setContents(signed_ext_value)

def LW(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets

    loaded_value = memLoad(memory, (rs1_val + imm), 4)

    registers[instructionAnd(instruction, 12, 7)].setContents(loaded_value)

def LBU(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets

    loaded_value = memLoad(memory, (rs1_val + imm), 1)

    registers[instructionAnd(instruction, 12, 7)].setContents(loaded_value)

def LHU(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed") # Load operations all use signed immediate-offsets

    loaded_value = memLoad(memory, (rs1_val + imm), 2)
    
    registers[instructionAnd(instruction, 12, 7)].setContents(loaded_value)

def SB(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    imm_upper = extractImmediate(instruction, 32, 25, "unsigned") << 5 # upper 7 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate

    signed_imm = extractedBinIntToSignedInt(imm_upper + imm_lower, 12)

    memStore(memory, (rs1_val + signed_imm), rs2_val, 1)

def SH(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    imm_upper = extractImmediate(instruction, 32, 25, "unsigned") << 5 # upper 7 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate

    signed_imm = extractedBinIntToSignedInt(imm_upper + imm_lower, 12)

    memStore(memory, (rs1_val + signed_imm), rs2_val, 2)

def SW(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    imm_upper = extractImmediate(instruction, 32, 25, "unsigned") << 5 # upper 7 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate

    signed_imm = extractedBinIntToSignedInt(imm_upper + imm_lower, 12)

    memStore(memory, (rs1_val + signed_imm), rs2_val, 4)


#LOAD IMMEADIATE
def LUI(instruction, registers):
    imm = extractImmediate(instruction, 32, 12, "unsigned")

    registers[instructionAnd(instruction, 12, 7)].setContents(imm<<12)

def AUIPC(instruction, registers, PC):
    imm = extractImmediate(instruction, 32, 12, "unsigned")

    registers[instructionAnd(instruction, 12, 7)].setContents(PC.getInstructionCounter() + (imm<<12))


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

def XORI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val ^ imm)

def ORI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val | imm)

def ANDI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val & imm)

def XOR(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val ^ rs2_val)

def OR(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val | rs2_val)

def AND(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val & rs2_val)


#Shift operations
def SLL(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val << rs2_val)

def SLLI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "unsigned")

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val << imm)

def SRLI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "unsigned")

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val >> imm)

def SRAI(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 25, 20, "signed")

    if rs1_val & 0x80000000:
        rs1_val -= 0x100000000

    rs1_val >>= imm
    
    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val & 0xFFFFFFFF)

def SRL(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val >> rs2_val)

def SRA(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    if rs1_val & 0x80000000:
        rs1_val -= 0x100000000

    rs1_val >>= rs2_val
    
    registers[instructionAnd(instruction, 12, 7)].setContents(rs1_val & 0xFFFFFFFF)


#Set operations
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

    if rs1 < imm:
        registers[instructionAnd(instruction, 12, 7)].setContents(1)
    else: 
        registers[instructionAnd(instruction, 12, 7)].setContents(0)


def SLTIU(instruction, registers):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    imm = extractImmediate(instruction, 32, 20, "unsigned")

    if rs1_val < imm:
        registers[instructionAnd(instruction, 12, 7)].setContents(1)
    else: 
        registers[instructionAnd(instruction, 12, 7)].setContents(0)


# Jump instructions
def JAL(instruction, registers, PC):
    imm = extractImmediate(instruction, 32, 12, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(PC+4)
    PC.addToProgramCounter(imm)

def JALR(instruction, registers, PC):
    imm = extractImmediate(instruction, 32, 12, "signed")

    registers[instructionAnd(instruction, 12, 7)].setContents(PC+4)
    PC.addToProgramCounter(imm)


#Branch instructions
def BEQ(instruction, registers, PC):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    signed_imm = extractedBinIntToSignedInt(extractBranchImmediate(instruction), 13)

    if rs1_val == rs2_val:
        PC.addToProgramCounter(int(signed_imm / 4) - 1)

def BNE(instruction, registers, PC):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    signed_imm = extractedBinIntToSignedInt(extractBranchImmediate(instruction), 13)

    if rs1_val != rs2_val:
        PC.addToProgramCounter(int(signed_imm / 4) - 1)

def BLT(instruction, registers, PC):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    signed_imm = extractedBinIntToSignedInt(extractBranchImmediate(instruction), 13)

    if rs1_val < rs2_val:
        PC.addToProgramCounter(int(signed_imm / 4) - 1)

def BGE(instruction, registers, PC):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()

    signed_imm = extractedBinIntToSignedInt(extractBranchImmediate(instruction), 13)

    if rs1_val >= rs2_val:
        PC.addToProgramCounter(int(signed_imm / 4) - 1)

def BLTU(instruction, registers, PC):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    raw_imm_bin = extractBranchImmediate(instruction)

    rs1_val = readAsUnsigned(rs1_val)
    rs2_val = readAsUnsigned(rs2_val)

    if rs1_val < rs2_val:
        PC.addToProgramCounter(int(raw_imm_bin / 4) - 1)

def BGEU(instruction, registers, PC):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    raw_imm_bin = extractBranchImmediate(instruction)

    rs1_val = readAsUnsigned(rs1_val)
    rs2_val = readAsUnsigned(rs2_val)

    if rs1_val >= rs2_val:
        PC.addToProgramCounter(int(raw_imm_bin / 4) - 1)


#Helper functions
def instructionAnd(instruction, upperBound, lowerBound, bit_width = 32) -> int:
    mask = (1 << bit_width) - 1
    instruction &= mask  # limit to 'bit_width' bits
    return (instruction & (2**upperBound-2**lowerBound))>>lowerBound

def extractImmediate(instruction, upperBound, lowerBound, immSign: str, bit_width = 32) -> int:
    """
    Bounds for extraction are: [lowerBound, upperBound[, i.e. lowerBound-bit is included, while upperBound-bit is NOT included.
    immSign:
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

# function from ChatGPT to extract immediate specifically from a branch operation
def extractBranchImmediate(instruction) -> int:
    imm12   = (instruction >> 31) & 0x1  # imm[12]
    imm11   = (instruction >> 7)  & 0x1  # imm[11]
    imm10_5 = (instruction >> 25) & 0x3F # imm[10:5]
    imm4_1  = (instruction >> 8)  & 0xF  # imm[4:1]

    return (imm12 << 12) | (imm11 << 11) | (imm10_5 << 5) | (imm4_1 << 1)


# stores given number of bytes in memory, starting at given address
def memStore(mem, address: int, value: int, numBytes: int):
    for i in range(numBytes):
        currentAddress = (address + i)
        currByte = value & 0xFF # extract first byte of value
        index = getAddressIndex(mem, currentAddress)
        if index > -1:
            mem[index].setMemoryContent(currByte)
        else:
            mem.append(addMemory(currentAddress, currByte))
        value = value >> 8 # remove byte we just read, and make the next byte the new first byte


# loads given number of bytes from memory, in the correct order, starting at given address, and returns the final value read as an int
def memLoad(mem, address: int, numBytes: int) -> int:
    res = 0
    # gets requested addresses from last address to first, so we get most significant value first, then least significant last
    # (range() excludes the upper-bound for the range, so "range(4, 0, -1)" would only return "[4, 3, 2, 1]", while we want '0' as well, so we use '-1' for upper-bound)
    for i in range(numBytes-1, -1, -1):
        # "res" gets left-shifted by 1 byte after each memFetch, since we read the most significant byte first, then the second-most significant, etc.
        res += memFetch(mem, (address + i)) << i*8

    return res

# tries to find content at given memory address and returns it if found; else, just returns '0'
def memFetch(mem, address: int) -> int:
    index = getAddressIndex(mem, address) # get memory list index of the address, if it exists ('-1' is returned if address wasn't in memory)
    if index > -1: # if valid index was returned:
        return mem[index].getMemoryContent() # return whatever content we've previously stored at this address
    return 0 # return '0' if we have yet to store anything at this address

# helper function to check if we already have a value at a given address, and returns the index of the item. Returns '-1' if address was not already in memory
def getAddressIndex(mem, address: int) -> int:
    for idx, i in enumerate(mem): # tracak both index and item in our 'mem' list
        if i.getMemoryAddress() == address:
            return idx # return index of list item if it's for the address we're looking for
    return -1 # return impossible index value in case given address wasn't already in our memory


# function from ChatGPT to convert signed bit string to its equivalent signed int value
# (e.g., the signed binary string, "11111110", would return "-2", while "011111110" would instead return "254")
def signedBinToInt(b: str) -> int:
    value = int(b, 2)           # convert bin → int (unsigned)
    bits = len(b)

    if value & (1 << (bits - 1)):   # if sign bit is set
        value -= 1 << bits         # subtract 2^bits

    return value

def extractedBinIntToSignedInt(int_val: int, max_len: int) -> int:
    raw_bin = bin(int_val)[2:]
    if len(raw_bin) < max_len:
        raw_bin = "0" + raw_bin
    return signedBinToInt(raw_bin)

def readAsUnsigned(val: int) -> int:
    if val < 0:
        val *= -1 # remove the Python-way of signing values (the minus-sign in front of values
        val_bin = "1" + bin(val)[2:] # add the normal way of signing values (a sign-bit as the most significant bit)
        return int(val_bin, 2)
    else:
        return val # if value was positive, nothing needs to be done, just return the value directly

# function taken from StackOverflow to convert signed int to corresponding two's-complement hex value
def signedIntToHex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))

# function from ChatGPT to sign-extend a binary string to become 32 bits wide
def sign_extend_to_32(b: str) -> str:
    sign_bit = b[0] # first bit = sign bit
    return sign_bit * (32 - len(b)) + b
