import sys
from collections import defaultdict

Coord = tuple[int, int]

class Number():
    def __init__(self, num: int, start: Coord, end: Coord) -> None:
        self.num: int = num
        self.isCounted: bool = False
        self.start: Coord = start
        self.end: Coord = end
    
    def __repr__(self) -> str:
        return f"{self.num} - {self.start=}, {self.end=}"

def load_file(filename: str = 'input.txt') -> list[str]:
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

def parseGrid(lines: list[str]) -> tuple[list[Number], set[Coord]]:
    nums: list[Number] = []
    specials: set[Coord] = set()
    for idx, line in enumerate(lines):
        currNum = ""
        i = 0
        while i < len(line):
            while i < len(line) and line[i].isnumeric():
                currNum += line[i]
                i += 1
            if currNum:
                nums.append(Number(int(currNum), (idx, i - len(currNum)), (idx, i-1)))
                currNum = ""
            if i < len(line) and not line[i].isnumeric() and line[i] != '.':
                 specials.add((idx, i))
            i += 1
    return nums, specials

def getGears(grid: list[str], nums: list[Number], specials: set[Coord]) -> dict[Coord, list[Number]]:
    parts: dict[Coord, list[Number]] = defaultdict(list)
    for s in specials:
        if grid[s[0]][s[1]] != '*': continue
        for n in nums:
            if isRunAdjacent(s, n.start, n.end):
                parts[s].append(n)
    return {k: v for k, v in parts.items() if len(v) == 2}

def isRunAdjacent(pos: Coord, start: Coord, end: Coord) -> bool:
    if abs(pos[0] - start[0]) > 1: return False
    if start[1] - 1 <= pos[1] <= end[1] + 1: return True
    return False        


def partOne():
    lines = load_file()
    nums, specials = parseGrid(lines)
    total = 0
    for n in nums:
        for s in specials:
            if isRunAdjacent(s, n.start, n.end):
                total += n.num
    print(total)

def partTwo():
    lines = load_file()
    nums, specials = parseGrid(lines)
    gears = getGears(lines, nums, specials)
    total = 0
    for a, b in gears.values():
        total += a.num * b.num
    print(total)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        partOne()
    elif sys.argv[1] == '2':
        partTwo()