from typing import List, Callable

from util import read_stripped_lines

def main() :
    orbitData = read_stripped_lines('input/day6.text')
    orbitData = list(map(lambda orbit : orbit.split(')'), orbitData))
    
    COM = makePlanet('COM', None, orbitData, 0)
    orbitCount = countOrbits(COM, 0)
    print(f'Orbit Count: {orbitCount}')

def findLowestParent(planet, moon1, moon2):
    # if any children can 
    if planet.isParent(moon1) and planet.isParent(moon2):
        pass

def isParent(parent, childName):
    for moon in parent.moon:
        if moon.name == childName:
            return True
        else: 
            return isParent(moon, childName)


def countOrbits(planet, orbitCount):
    moonOrbitCount = 0
    for moon in planet.moons:
        moonOrbitCount += countOrbits(moon, orbitCount)
    return orbitCount + moonOrbitCount + planet.orbits

def makePlanet(name, planetParent, orbitData, orbits):
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