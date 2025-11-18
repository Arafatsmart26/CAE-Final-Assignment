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
    signed_ext_value = int(sign_extend_to_32(bin(loaded_value)[2:]), 2)

    registers[instructionAnd(instruction, 12, 7)].setContents(signed_ext_value)

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

    raw_imm_bin = bin(imm_upper + imm_lower)[2:]
    if len(raw_imm_bin) < 12:
        raw_imm_bin = "0" + raw_imm_bin
    signed_imm = signedBinToInt(raw_imm_bin)

    memStore(memory, (rs1_val + signed_imm), rs2_val, 1)

def SH(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    imm_upper = extractImmediate(instruction, 32, 25, "unsigned") << 5 # upper 7 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate

    raw_imm_bin = bin(imm_upper + imm_lower)[2:]
    if len(raw_imm_bin) < 12:
        raw_imm_bin = "0" + raw_imm_bin
    signed_imm = signedBinToInt(raw_imm_bin)

    memStore(memory, (rs1_val + signed_imm), rs2_val, 2)

def SW(instruction, registers, memory):
    rs1_val = registers[instructionAnd(instruction, 20, 15)].getContents()
    rs2_val = registers[instructionAnd(instruction, 25, 20)].getContents()
    imm_upper = extractImmediate(instruction, 32, 25, "unsigned") << 5 # upper 7 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate
    imm_lower = extractImmediate(instruction, 12, 7, "unsigned") # lower 5 bits of the immediate

    raw_imm_bin = bin(imm_upper + imm_lower)[2:]
    if len(raw_imm_bin) < 12:
        raw_imm_bin = "0" + raw_imm_bin
    signed_imm = signedBinToInt(raw_imm_bin)

    memStore(memory, (rs1_val + signed_imm), rs2_val, 4)


#LOAD IMMEADIATE
def LUI(instruction, registers):
    imm = extractImmediate(instruction, 32, 12, "unsigned")

    registers[instructionAnd(instruction, 12, 7)].setContents(imm<<12)




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


# function from ChatGPT to sign-extend a binary string to become 32 bits wide
def sign_extend_to_32(b: str) -> str:
    sign_bit = b[0]                     # first bit = sign bit
    return sign_bit * (32 - len(b)) + b