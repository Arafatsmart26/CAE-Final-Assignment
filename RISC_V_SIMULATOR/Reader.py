size = 4
instructions = []
scale = 16
num_of_bits = 32

with open('RISC_V_SIMULATOR/tests/task1/addlarge.bin', 'rb') as f:
    while True:
        chunk = f.read(size)
        if not chunk:
            break
        instructions.append(bin(int(chunk.hex(),scale))[2:].zfill(num_of_bits))

for i in instructions:
    print(i)
print(len(instructions))