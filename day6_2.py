class Planet:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet  # parent
        self.moons = []  # parent

    def add_moon(self, moon):
        pass


def map_planets(orbit_data):
    pass


def main():
    filename = "input/day6_test.txt"
    with open(filename) as file:
        planet_dict = {}
        for orbit in file.readlines():
            print(orbit)


main()
