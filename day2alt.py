import intcodeComputer

intcode = intcodeComputer.parseInputFile('input/day2.text')
intcode = intcodeComputer.runProgram(intcode)
print(intcode[0])