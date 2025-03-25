from util import read_stripped_lines


def main():
    wirePaths = read_stripped_lines('input/day3.txt')
    wirePaths = list(map(lambda element: element.split(','), wirePaths))
    wireHistories = []

    for wirePath in wirePaths:
        pathHistory = []
        lastPosition = Position(0, 0, 0)
        for instruction in wirePath:
            for _ in range(int(instruction[1:])):
                lastPosition = completeInstruction(instruction[0], lastPosition)
                pathHistory.append(lastPosition)
        wireHistories.append(pathHistory)

    # TODO: check each point in each wire history for all intersection points, then find the manhatten distance from those points (add x and y)
    intersections = []
    for firstPosition in wireHistories[0]:
        for secondPosition in wireHistories[1]:
            if firstPosition.x == secondPosition.x and firstPosition.y == secondPosition.y:
                intersections.append(Position(firstPosition.x, firstPosition.y, firstPosition.steps+secondPosition.steps))

    # lengths = list(map(lambda position: abs(position[0]) + abs(position[1]), intersections))
    lengths = list(map(lambda position: position.steps, intersections))
    print(f'Min Dist: {min(lengths)}')
    # 165 too low


def completeInstruction(direction: str, lastPosition: tuple) -> tuple:
    if direction == 'U':
        return Position(lastPosition.x, lastPosition.y+1, lastPosition.steps+1)
    elif direction == 'D':
        return Position(lastPosition.x, lastPosition.y-1, lastPosition.steps+1)
    elif direction == 'R':
        return Position(lastPosition.x+1, lastPosition.y, lastPosition.steps+1)
    elif direction == 'L':
        return Position(lastPosition.x-1, lastPosition.y, lastPosition.steps+1)
    else:
        print(f'Invalid path instruction {direction}')


class Position:
    def __init__(self, x: int, y: int, steps: int) -> None:
        self.x = x
        self.y = y
        self.steps = steps


if __name__ == '__main__':
    main()
