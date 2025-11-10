from logicOperations import ADD
from Registers import *
registers=Initialize()
def Interpreter(instruction):
    opcode = instruction[25:32] #We take the last 7 bits which is the opcode. Python includes the lower bound but excludes the upper
    funct3 = instruction[17:20] #Not all instructions have a funct3 or funct7 field but we define it here as it is always the same place
    funct7 = instruction[0:7] #If the instruction doesn't use these fields, it won't call these variables anyway
    match opcode[0:3]: #In order to be more effective the match statement uses the first 3 bits so that every instruction runs more effectively
        case "001":
            match opcode:
                case "0010111": #AUIPC
                    print("AUIPC")
                case "0010011": #Logic immeadiate operations
                    match funct3:
                        case "000": #ADDI
                            print("ADDI")
                        case "010": #SLTI
                            print("SLTI")
                        case "011": #SLTIU
                            print("SLTIU")
                        case "100": #XORI
                            print("XORI")
                        case "110": #ORI 
                            print("ORI")
                        case "111": #ANDI
                            print("ANDI")
                        case "001": #SLLI
                            print("SLLI")
                        case "101": #SRLI | SRAI
                            match funct7:
                                case "0000000": #SRLI
                                    print("SRLI")
                                case "0100000": #SRAI
                                    print("SRAI")
        
        case "011":
            match opcode:
                case "0110111": #LUI
                    print("LUI")
                case "0110011": #Logic operations
                    match funct3:
                        case "000": #ADD | SUB
                            match funct7:
                                case "0000000": #ADD
                                    ADD.ADD(instruction, registers)
                                    print("ADD")
                                case "0100000": #SUB
                                    print("SUB")
                        case "001": #SLL
                            print("SLL")
                        case "010": #SLT
                            print("SLT")
                        case "011": #SLTU
                            print("SLTU")
                        case "100": #XOR
                            print("XOR")
                        case "101": #SRL | SRA
                            match funct7:
                                case "0000000": #SRL
                                    print("SRL")
                                case "0100000": #SRA
                                    print("SRA")
                        case "110": #OR
                            print("OR")
                        case "111": #AND
                            print("AND")

        case "110":
            match opcode:
                case "1101111": #JAL
                    print("JAL")
                case "1100111": #JALR
                    print("JALR")
                case "1100011": #Branching
                    match funct3:
                        case "000": #BEQ
                            print("BEQ")
                        case "001": #BNE
                            print("BNE")
                        case "100": #BLT
                            print("BLT")
                        case "101": #BGE
                            print("BGE")
                        case "110": #BLTU
                            print("BLTU")
                        case "111": #BGEU
                            print("BGEU")
        case "000": #load operations
            match funct3:
                case "000": #LB
                    print("LB")
                case "001": #LH
                    print("LH")
                case "010": #LW
                    print("LW")
                case "100": #LBU
                    print("LBU")
                case "101": #LHU
                    print("LHU")

        case "010": # save immeadiate operations
            match funct3:
                case "000": #SB
                    print("SB")
                case "001": #SH
                    print("SH")
                case "010": #SW
                    print("SW")
        case "111":
            #ECall method
            print("ECall")
    return registers


        

        

        
