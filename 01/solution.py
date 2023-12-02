import sys
WORD_NUMS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def load_file(filename: str = 'input.txt') -> list[str]:
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

def partOne():
    words = load_file()
    res = 0
    for w in words:
        for i in range(len(w)):
            if w[i].isnumeric():
                first = int(w[i])
                break
        
        for i in range(len(w)-1, -1, -1):
            if w[i].isnumeric():
                last = int(w[i])
                break
        res += first * 10 + last
    print(res)

def partTwo():
    words = load_file()
    res = 0
    for w in words:
        for i in range(len(w)):
            if w[i].isnumeric():
                first = int(w[i])
                break
            elif wn := isWordNum(w, i, True):
                first = wn
                break
        
        for i in range(len(w)-1, -1, -1):
            if w[i].isnumeric():
                last = int(w[i])
                break
            elif wn := isWordNum(w, i, False):
                last = wn
                break
        res += first * 10 + last
    print(res)

def isWordNum(word, idx, forward):
    if forward:
        for wn, n in WORD_NUMS.items():
            if word[idx:idx+len(wn)] == wn: return n
    else:
        for wn, n in WORD_NUMS.items():
            if word[idx-len(wn)+1:idx+1] == wn: return n
    return 0

if __name__ == '__main__':
    if sys.argv[1] == '1':
        partOne()
    elif sys.argv[1] == '2':
        partTwo()