from typing import List, Callable

from util import read_stripped_lines

# Check if santa is below you (in the tree), if not, move up. 
# Repeat until Santa is found. Move down. 

def main() :
    orbitData = read_stripped_lines('input/day6.text')
    orbitData = list(map(lambda orbit : orbit.split(')'), orbitData))
    
    COM = makePlanet('COM', None, orbitData, 0)
    # part 1 vvv
    # orbitCount = countOrbits(COM, 0)
    # print(f'Orbit Count: {orbitCount}')
    
    #part 2 vvv
    # findDistanceBetweenMoons(COM, 'YOU', 'SAN')
    print(f'YOU is child of COM: {isParent(COM, "YOU")}')

def findDistanceBetweenMoons(planet: Callable, moonName1: str, moonName2: str, distance: int = None) -> int: 
    distance1 = findMoonDistance(planet, moonName1)
    distance2 = findMoonDistance(planet, moonName2)
    if distance1 + distance2 < 0:
        return distance
    for moon in planet.moons:
        findDistanceBetweenMoons(moon, moonName1, moonName2, distance1+distance2)

def findMoonDistance(planet: Callable, moonName: Callable, orbitDistance: int = 1) -> int:
    for moon in planet.moons:
        if moon.name == moonName:
            return orbitDistance
        return findMoonDistance(moon, moonName, orbitDistance+1)       

def findLowestParent(planet, moon1, moon2):
    # if any children can 
    if planet.isParent(moon1) and planet.isParent(moon2):
        pass

def isParent(parent, childName):
    if len(parent.moons) <= 0:
        return None
    for moon in parent.moons:
        if moon.name == childName:
            return True
        foundMoon = isParent(moon, childName)
        if foundMoon == True:
            return foundMoon
        elif foundMoon == False:
            return foundMoon
        elif foundMoon == None:
            return foundMoon

def countOrbits(planet, orbitCount):
    moonOrbitCount = 0
    for moon in planet.moons:
        moonOrbitCount += countOrbits(moon, orbitCount)
    return orbitCount + moonOrbitCount + planet.orbits

def makePlanet(name, planetParent, orbitData, orbits):
    if name == 'YOU':
        print('YOU found')
    if name == 'SAN':
        print('SAN found')
    moonNames = findMoonNames(name, orbitData)
    moons=[]
    planet = Planet(name, planetParent, moons, orbits)
    for moonName in moonNames:
        moons.append(makePlanet(moonName, planet, orbitData, planet.orbits+1))
    planet.moons = moons
    return planet

def findMoonNames(planetName: str, orbitData: List[List[str]]) -> List[str]:
    moons = []
    for index, orbit in enumerate(orbitData):
        if orbit[0] == planetName:
            moons.append(orbit[1])
    return moons

class Planet:
    def __init__(self, name: str, planet: Callable, moons: List[Callable], orbits: int):
        self.name = name
        self.planet = planet
        self.moons = moons
        self.orbits = orbits

    def addMoon(self, moon: Callable):
       self.moons.append(moon)

if __name__ == '__main__':
    main()