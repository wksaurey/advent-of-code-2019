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

3 - 0 modes, 1 param
    Desc: takes a single int as input and puts it in the input address
    param1: address to put input int

4 - up to 1 mode, 1 param
    Desc: outputs the value at the input address
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    param1: address of the number to be output

5 - up to 2 modes, 2 params
    Desc, if param1 is non-zero, change pointer (index) to param2
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    mode2: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    param1: zero or non-zero (true or false)
    param2: value to change the pointer (index) to

6 - up to 2 modes, 2 params
    Desc, if param1 is zero, change pointer (index) to param2
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    mode2: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    param1: zero or non-zero (true or false but reverse of opcode 5)
    param2: value to change the pointer (index) to

7 - up to 3 modes, 3 params
    Desc: if param1 is less than param2 store 1 in the address of param3
        else, store 0
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    mode2: 
        0: param2 is in position mode
        1: param2 is in immediate mode
    mode3:
        0: param3 will always be in position mode
    param1: first number to compare to the second
    param2: second number to compare to the first
    param3: address to save 1 or 0
    
8 - up to 3 modes, 3 params
    Desc: if param1 is equal t0 param2 store 1 in the address of param3
        else, store 0
    mode1: 
        0: param1 is in position mode
        1: param1 is in immediate mode
    mode2: 
        0: param2 is in position mode
        1: param2 is in immediate mode
    mode3:
        0: param3 will always be in position mode
    param1: first number to compare to the second
    param2: second number to compare to the first
    param3: address to save 1 or 0

99 - 0 modes, 0 params
    ends the program
'''

testIntcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
ADDRESSMODE = 0
INSTANTMODE = 1

def main():
    runProgram(testIntcode)

def parseInputFile(filename: str) -> List[int]:
    print(f'Reading from file {filename}')
    intcode = open(filename).readline()
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
                param1 = getNumber(intcode, modes[2], index)
                index+=1
                param2 = getNumber(intcode, modes[1], index)
                index+=1
                param3 = getNumber(intcode, INSTANTMODE, index)
                intcode[param3] = param1 + param2
            case 2:
                index+=1
                param1 = getNumber(intcode, modes[2], index) 
                index+=1
                param2 = getNumber(intcode, modes[1], index)
                index+=1
                param3 = getNumber(intcode, INSTANTMODE, index)
                intcode[param3] = param1 * param2
            case 3:
                print('Opcode 3 input: ', end='')
                userInput = int(input())
                print()
                index+=1
                param1 = getNumber(intcode, INSTANTMODE, index)
                intcode[param1] = userInput
            case 4:
                index+=1
                param1 = getNumber(intcode, modes[2], index)
                print(f'Opcode 4 output: {param1}')
            case 5:
                index+=1
                param1 = getNumber(intcode, modes[2], index) 
                index+=1
                param2 = getNumber(intcode, modes[1], index)
                if param1 != 0:
                    index = param2 - 1
            case 6:
                index+=1
                param1 = getNumber(intcode, modes[2], index) 
                index+=1
                param2 = getNumber(intcode, modes[1], index)
                if param1 == 0:
                    index = param2 - 1
            case 7:
                index+=1
                param1 = getNumber(intcode, modes[2], index) 
                index+=1
                param2 = getNumber(intcode, modes[1], index)
                index+=1
                param3 = getNumber(intcode, INSTANTMODE, index)
                if param1 < param2:
                    intcode[param3] = 1
                else:
                    intcode[param3] = 0
            case 8:
                index+=1
                param1 = getNumber(intcode, modes[2], index) 
                index+=1
                param2 = getNumber(intcode, modes[1], index)
                index+=1
                param3 = getNumber(intcode, INSTANTMODE, index)
                if param1 == param2:
                    intcode[param3] = 1
                else:
                    intcode[param3] = 0
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

def getNumber(intcode: List[int], mode: str, index: int):
    mode = int(mode)
    param = intcode[index]
    match mode:
        case 0: # AddressMode
            return intcode[param]
        case 1: # InstantMode
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