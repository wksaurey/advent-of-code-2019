from util import read_stripped_lines

def main():
    wirePaths = read_stripped_lines('input/day3.text')
    wirePaths = list(map(lambda element: element.split(','), wirePaths))
    wireHistories = []

    for wirePath in wirePaths:
        pathHistory = []
        lastPosition = (0, 0)
        for instruction in wirePath:
            for index in range(int(instruction[1])):
                lastPosition = completeInstruction(instruction, lastPosition)
                pathHistory.append(lastPosition)
        wireHistories.append(pathHistory)

    print(len(wireHistories))
    # TODO: check each point in each wire history for all intersection points, then find the manhatten distance from those points (add x and y)

def completeInstruction(instruction: str, lastPosition: tuple) -> tuple:
    if instruction[0] == 'U':
        return (lastPosition[0], lastPosition[1]+1)
    elif instruction[0] == 'D':
        return (lastPosition[0], lastPosition[1]-1)
    elif instruction[0] == 'R':
        return (lastPosition[0]+1, lastPosition[1])
    elif instruction[0] == 'L':
        return (lastPosition[0]-1, lastPosition[1])
    else:
        print(f'Invalid path instruction {instruction[0]}')

if __name__ == '__main__':
    main()