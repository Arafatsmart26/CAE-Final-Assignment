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


def getRegisters():
    return registers
