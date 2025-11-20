from logicOperations import *
from Registers import *
from Program_Counter import *

def Interpreter(instruction, registers, memory, program_counter):
    # print("instruction: " + format(instruction, '032b'))
    program_counter = program_counter
    opcode = instructionAnd(instruction, 7, 0) #We take the last 7 bits which is the opcode. Python includes the lower bound but excludes the upper
    funct3 = instructionAnd(instruction, 15, 12) #Not all instructions have a funct3 or funct7 field but we define it here as it is always the same place
    funct7 = instructionAnd(instruction, 32, 25) #If the instruction doesn't use these fields, it won't call these variables anyway
    match instructionAnd(instruction, 7, 4): #In order to be more effective the match statement uses the first 3 bits so that every instruction runs more effectively
        case 1:
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
                            SLTI(instruction, registers)
                        case 3: #SLTIU
                            print("SLTIU")
                            SLTIU(instruction, registers)
                        case 4: #XORI
                            print("XORI")
                            XORI(instruction, registers)
                        case 6: #ORI 
                            print("ORI")
                            ORI(instruction, registers)
                        case 7: #ANDI
                            print("ANDI")
                            ANDI(instruction, registers)
                        case 1: #SLLI
                            print("SLLI")
                            SLLI(instruction, registers)
                        case 5: #SRLI | SRAI
                            match funct7:
                                case 0: #SRLI
                                    print("SRLI")
                                    SRLI(instruction, registers)
                                case 32: #SRAI
                                    print("SRAI")
                                    SRAI(instruction, registers)#Doesn't work
        
        case 3:
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
                                    SUB(instruction, registers)
                        case 1: #SLL
                            print("SLL")
                            SLL(instruction, registers)
                        case 2: #SLT
                            print("SLT")
                            SLT(instruction, registers)
                        case 3: #SLTU
                            print("SLTU")
                            SLTU(instruction, registers)
                        case 4: #XOR
                            print("XOR")
                            XOR(instruction, registers)
                        case 5: #SRL | SRA
                            match funct7:
                                case 0: #SRL
                                    print("SRL")
                                    SRL(instruction, registers)
                                case 32: #SRA
                                    print("SRA")
                                    SRA(instruction, registers)#Doesn't work
                        case 6: #OR
                            print("OR")
                            OR(instruction, registers)
                        case 7: #AND
                            print("AND")
                            AND(instruction, registers)

        case 6:
            match opcode:
                case 111: #JAL
                    print("JAL")
                case 103: #JALR
                    print("JALR")
                case 99: #Branching
                    match funct3:
                        case 0: #BEQ
                            print("BEQ")
                            BEQ(instruction, registers, program_counter)
                        case 1: #BNE
                            print("BNE")
                            BNE(instruction, registers, program_counter)
                        case 4: #BLT
                            print("BLT")
                            BLT(instruction, registers, program_counter)
                        case 5: #BGE
                            print("BGE")
                            BGE(instruction, registers, program_counter)
                        case 6: #BLTU
                            print("BLTU")
                            BLTU(instruction, registers, program_counter)
                        case 7: #BGEU
                            print("BGEU")
                            BGEU(instruction, registers, program_counter)
        case 0: #load operations
            match funct3:
                case 0: #LB
                    print("LB")
                    LB(instruction, registers, memory)
                case 1: #LH
                    print("LH")
                    LH(instruction, registers, memory)
                case 2: #LW
                    print("LW")
                    LW(instruction, registers, memory)
                case 4: #LBU
                    print("LBU")
                    LBU(instruction, registers, memory)
                case 5: #LHU
                    print("LHU")
                    LHU(instruction, registers, memory)

        case 2: # save immeadiate operations
            match funct3:
                case 0: #SB
                    print("SB")
                    SB(instruction, registers, memory)
                case 1: #SH
                    print("SH")
                    SH(instruction, registers, memory)
                case 2: #SW
                    print("SW")
                    SW(instruction, registers, memory)
        case 7:
            #ECall method
            print("ECall")

    if registers[0].getContents() != 0:
        registers[0].setContents(0)
        


        

        

        
