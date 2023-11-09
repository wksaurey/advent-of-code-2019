import intcodeComputer

intcode = intcodeComputer.parseInputFile('input/day2.test')
intcode = intcodeComputer.runProgram(intcode)
print(intcode[0])