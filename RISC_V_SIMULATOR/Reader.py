def Reader(filename):
    size = 4 #Defines how many bytes we will read at a time. 
    instructions = [] #We initializa the array that will hold our instructions
    scale = 16 #This number is used to tell the int function that the number it parses is in base 16
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(size) #Each chunk is 4 bytes
            if not chunk: #This checks if the chunk is empty, if it is we break the while loop
                break
            chunk = chunk[::-1]
            instructions.append(int(chunk.hex(),scale)) #We convert the hexcode to binary, remove the prefix and fills in extra bits if needed

    return instructions
