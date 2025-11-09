from Interpreter import Interpreter
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
            chunk = chunk[::-1] #Reverses the order of the bits we read so that we attach them in the right order as RISC-V reads the instruction starting from the right
            instructions.append(bin(int(chunk.hex(),scale))[2:].zfill(num_of_bits)) #We convert the hexcode to binary, remove the prefix and fills in extra bits if needed
    return instructions
for i in Reader():
    print(i)
print(len(Reader()))
for i in Reader():
    Interpreter(i)
