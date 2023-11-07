from typing import List

def read_stripped_lines(path: str, chars: str = "\n") -> List[str]:
    with open(path) as f:
        return list(map(lambda line: line.strip(chars), f.readlines()))

def manhattanDistance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1-x2) + abs(y1-y2)