import sys
from math import prod
from collections import defaultdict

def load_file(filename: str = 'input.txt') -> list:
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

def partOne():
    lines = load_file()
    res = 0
    for idx, line in enumerate(lines):
        if isGamePossible(line): res += idx+1
    print(res)

def partTwo():
    lines = load_file()
    res = 0
    for line in lines:
        res += calcPower(line)
    print(res)

def isGamePossible(line: str) -> bool:
    for n, c in parseLine(line):
        if n > 12 and c == "red" or n > 13 and c == "green" or n > 14 and c == "blue":
            return False
    return True

def parseLine(line: str) -> list[int, str]:
    sets = line.split(':')[1].split(';')
    vals: list[int, str] = []
    for s in sets:
        infos = s.split(', ')
        for info in infos:
            n, c = info.split()
            vals.append((int(n), c))
    return vals

def calcPower(line: str) -> int:
    maxs = defaultdict(int)
    for n, c in parseLine(line):
        maxs[c] = max(maxs[c], n)
    return prod(v for v in maxs.values())
    
if __name__ == '__main__':
    if sys.argv[1] == '1':
        partOne()
    elif sys.argv[1] == '2':
        partTwo()