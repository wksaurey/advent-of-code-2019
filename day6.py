from typing import List, Callable

from util import read_stripped_lines

def main() :
    orbitData = read_stripped_lines('input/day6.text')
    orbitData = list(map(lambda orbit : orbit.split(')'), orbitData))
    print(orbitData)

    planets = set()
    root
    for orbit in orbitData:
        orbitPlanet = orbit[0]
        orbitMoon = orbit[1]
        planet = Planet(orbitPlanet, [orbitMoon])
        planets.add(planet)
        if planet.name == 'COM':
            root = planet


class Planet:
    def __init__(self, planetName: str, moons: List[Callable]):
        self.planetName = planetName
        self.moons = moons

    def addMoon(self, moon: Callable):
       self.moons.append(moon)

if __name__ == '__main__':
    main()