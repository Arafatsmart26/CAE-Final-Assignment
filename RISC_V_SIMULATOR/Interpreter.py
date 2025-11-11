from logicOperations import *
from Registers import *
registers=Initialize()
memory = []
def Interpreter(instruction):
    opcode = instruction & 2**7-2**0 #We take the last 7 bits which is the opcode. Python includes the lower bound but excludes the upper
    #print("this is the opcode " + str(opcode))
    funct3 = instruction & 2**15-2**12 #Not all instructions have a funct3 or funct7 field but we define it here as it is always the same place
    funct7 = instruction & 2**32-2**25 #If the instruction doesn't use these fields, it won't call these variables anyway
    #print(opcode & 2**7-(2**4))
    match opcode & 2**7-2**4: #In order to be more effective the match statement uses the first 3 bits so that every instruction runs more effectively
        case 16:
            match opcode:
                case 23: #AUIPC
                    print("AUIPC")
                case 19: #Logic immeadiate operations
                    match funct3:
                        case 0: #ADDI
                            print("ADDI")
                            ADDI(instruction, registers)
                        case 2: #SLTI
                            print("SLTI")
                        case 3: #SLTIU
                            print("SLTIU")
                        case 4: #XORI
                            print("XORI")
                        case 6: #ORI 
                            print("ORI")
                        case 7: #ANDI
                            print("ANDI")
                        case 1: #SLLI
                            print("SLLI")
                        case 5: #SRLI | SRAI
                            match funct7:
                                case 0: #SRLI
                                    print("SRLI")
                                case 32: #SRAI
                                    print("SRAI")
        
        case 48:
            match opcode:
                case 55: #LUI
                    print("LUI")
                    LUI(instruction, registers)
                case 51: #Logic operations
                    match funct3:
                        case 0: #ADD | SUB
                            match funct7:
                                case 0: #ADD
                                    print("ADD")
                                    ADD(instruction, registers)
                                case 32: #SUB
                                    print("SUB")
                        case 1: #SLL
                            print("SLL")
                        case 2: #SLT
                            print("SLT")
                        case 3: #SLTU
                            print("SLTU")
                        case 4: #XOR
                            print("XOR")
                        case 5: #SRL | SRA
                            match funct7:
                                case 0: #SRL
                                    print("SRL")
                                case 32: #SRA
                                    print("SRA")
                        case 6: #OR
                            print("OR")
                        case 7: #AND
                            print("AND")

        case 96:
            match opcode:
                case 111: #JAL
                    print("JAL")
                case 103: #JALR
                    print("JALR")
                case 99: #Branching
                    match funct3:
                        case 0: #BEQ
                            print("BEQ")
                        case 1: #BNE
                            print("BNE")
                        case 4: #BLT
                            print("BLT")
                        case 5: #BGE
                            print("BGE")
                        case 6: #BLTU
                            print("BLTU")
                        case 7: #BGEU
                            print("BGEU")
        case 0: #load operations
            match funct3:
                case 0: #LB
                    print("LB")
                case 1: #LH
                    print("LH")
                case 2: #LW
                    print("LW")
                case 4: #LBU
                    print("LBU")
                case 5: #LHU
                    print("LHU")

        case 32: # save immeadiate operations
            match funct3:
                case 0: #SB
                    print("SB")
                case 1: #SH
                    print("SH")
                case 2: #SW
                    print("SW")
        case 112:
            #ECall method
            print("ECall")
def getRegisters():
    return registers
        


        

        

        
