import intcodeComputer

intcode = intcodeComputer.parseInputFile('input/day2.txt')
intcode = intcodeComputer.runProgram(intcode)
print(intcode[0])
