from util import read_stripped_lines


def runProgram(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    index = 0
    while(True):
        opcode = intcode[index]
        firstAddress = intcode[index+1]
        secondAddress = intcode[index+2]
        outputAddress = intcode[index+3]
        if(outputAddress >= len(intcode)):
            break
        
        firstNumber = intcode[firstAddress]
        secondNumber = intcode[secondAddress]

        if opcode == 1:
            intcode[outputAddress] = firstNumber + secondNumber
        elif opcode == 2:
            intcode[outputAddress] = firstNumber * secondNumber
        elif opcode == 99:
            break
        else:
            print(f'Invalid opcode {opcode}')
            break

        index += 4

    return intcode[0]

for noun in range(0, 100):
    for verb in range(0, 100):
        intcode = open('input/day2.text').readline()
        intcode = list(map(lambda element: int(element), intcode.split(',')))
        if runProgram(intcode, noun, verb) == 19690720:
            print(f'Noun: {noun}')
            print(f'Verb: {verb}')
            print(f'Function Output: {100 * noun + verb}')
            break