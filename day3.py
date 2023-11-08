from util import read_stripped_lines

def main():
    wirePaths = read_stripped_lines('input/day3test.text')
    wirePaths = list(map(lambda element: element.split(','), wirePaths))
    wireHistories = []

    for wirePath in wirePaths:
        pathHistory = []
        lastPosition = (0, 0)
        for instruction in wirePath:
            for _ in range(int(instruction[1:])):
                lastPosition = completeInstruction(instruction[0], lastPosition)
                pathHistory.append(lastPosition)
        wireHistories.append(pathHistory)

    # TODO: check each point in each wire history for all intersection points, then find the manhatten distance from those points (add x and y)
    intersections = []
    for firstPosition in wireHistories[0]:
        for secondPosition in wireHistories[1]:
            if firstPosition == secondPosition:
                intersections.append(firstPosition)

    print(intersections)
    lengths = list(map(lambda position: abs(position[0]) + abs(position[1]), intersections))
    print(f'Min Dist: {min(lengths)}')
    # 165 too low

def completeInstruction(direction: str, lastPosition: tuple) -> tuple:
    if direction == 'U':
        return (lastPosition[0], lastPosition[1]+1)
    elif direction == 'D':
        return (lastPosition[0], lastPosition[1]-1)
    elif direction == 'R':
        return (lastPosition[0+1], lastPosition[1])
    elif direction == 'L':
        return (lastPosition[0]-1, lastPosition[1])
    else:
        print(f'Invalid path instruction {direction}')

if __name__ == '__main__':
    main()
