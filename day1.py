import math

from util import read_stripped_lines


def calculateFuel(mass):
    mass = int(mass)
    fuel = math.trunc(mass/3) - 2
    if fuel < 0:
        return 0
    return fuel + calculateFuel(fuel)


def getFuel(mass):
    totalFuel = 0
    for module in modules:
        totalFuel += calculateFuel(module)
    return totalFuel


modules = read_stripped_lines('input/day1.txt')
print(getFuel(modules))
