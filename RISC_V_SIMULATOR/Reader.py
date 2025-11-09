from Interpreter import Interpreter
def Reader():
    size = 4
    instructions = []
    scale = 16
    num_of_bits = 32

    with open('RISC_V_SIMULATOR/tests/task1/addlarge.bin', 'rb') as f:
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            chunk = chunk[::-1]
            instructions.append(bin(int(chunk.hex(),scale))[2:].zfill(num_of_bits))
    return instructions
for i in Reader():
    print(i)
print(len(Reader()))
for i in Reader():
    Interpreter(i)

