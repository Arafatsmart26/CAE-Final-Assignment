import glob
import os
from Reader import Reader

def Tester():
    base_path = os.path.join("RISC_V_SIMULATOR", "tests", "task1", "*.bin")

    for filename in glob.glob(base_path):
        print(f"Reading file: {filename}")
        Reader(filename)
print(Tester())