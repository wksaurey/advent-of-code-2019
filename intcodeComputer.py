from typing import List

'''
Opcodes
1 - up to 3 modes, 3 params
    Desc: 
        adds the two numbers given by the first two params and
        saves it in memory at the address given by the third param
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    mode2: 
        0: param2 is in position mode
        1: param2 is in immediate mode
    mode3:
        0: param3 will always be in position mode
    param1: first number to add
    param2: second number to add
    param3: address to save sum

2 - up to 3 modes, 3 params
    Desc:
        multiplies the two numbers given by the first two params and
        puts the result in the address given by the third param
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    mode2: 
        0: param2 is in position mode
        1: param2 is in immediate mode
    mode3:
        0: param3 will always be in position mode
    param1: first number to multiply 
    param2: second number to multiply
    param3: address to save product

3 - up to 1 mode, 1 param
    Desc: takes a single int as input and puts it in the input address
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    param1: address to put input int

4 - up to 1 mode, 1 param
    Desc: outputs the value at the input address
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    param1: address of the number to be output

99 - 0 modes, 0 params
    ends the program
'''

testIntcode = [1002,4,3,4,33]

def main():
    runProgram()

def parseInputFile(filename: str) -> List[int]:
    intcode = open('input/day2.text').readline()
    intcode = list(map(lambda element: int(element), intcode.split(',')))
    return intcode

def runProgram(intcode):
    print('Welcome to Intcode Computer')
    index = 0
    while(True):
        opcode = int(str(intcode[index])[-2:])
        modes = getModes(str(intcode[index])[:-2])

        match opcode:
            case 1:
                index+=1
                param1 = getNumber(intcode, modes[2], intcode[index])
                index+=1
                param2 = getNumber(intcode, modes[1], intcode[index])
                index+=1
                param3 = getNumber(intcode, 1, intcode[index])
                intcode[param3] = param1 + param2
            case 2:
                index+=1
                param1 = getNumber(intcode, modes[2], intcode[index])
                index+=1
                param2 = getNumber(intcode, modes[1], intcode[index])
                index+=1
                param3 = getNumber(intcode, 1, intcode[index])
                intcode[param3] = param1 * param2
            case 3:
                pass
            case 4:
                pass
            case 99:
                message = 'Exiting program due to opcode 99\n'
                print(message)
                break
            case _:
                message = f'Invalid opcode {opcode}\n'
                print(message)
                break

        index += 1
    return(intcode)

def getNumber(intcode: List[int], mode: str, param: int):
    mode = int(mode)
    match mode:
        case 0:
            return intcode[param]
        case 1:
            return param

def getModes(modes):
    if modes == '':
        return '000'
    elif len(modes) == 3:
        return modes
    elif len(modes) < 3:
        return getModes('0' + modes)
    else:
        print(f'Invalid modes {modes}')
        return
    
        



if __name__ == '__main__':
    main()