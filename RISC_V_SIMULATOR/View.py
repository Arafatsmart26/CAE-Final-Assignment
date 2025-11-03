size = 4
bytes = []
scale=16
num_of_bits=32
with open(r'C:\Users\simon\Documents\DTU\RISC_V_SIMULATOR\addlarge.bin', 'rb') as f:
    while True:
        chunk = f.read(size)
        if not chunk:
            break
        bytes.append(bin(int(chunk.hex(),scale))[2:].zfill(num_of_bits))

for i in bytes:
    print(i)
print(len(bytes))