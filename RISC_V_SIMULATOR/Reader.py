
def Reader():
    size = 1
    instructions = []
    scale = 16
    with open('RISC_V_SIMULATOR/tests/task1/addlarge.bin', 'rb') as f:
        while True:
            instruction = []
            for i in range(0,4):
                chunk = f.read(size)
                if not chunk:
                    break
                instruction.append(int(chunk.hex(),scale))
            if not chunk:
                    break
            instructions.append(instruction)
    return instructions
print(len(Reader()))
for i in Reader():
    print(i)