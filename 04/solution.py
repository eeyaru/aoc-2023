import sys

def load_file(filename: str = 'sample.txt') -> list:
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

def parseCards(cards: list[str]) -> list[tuple[set[int], set[int]]]:
    parsedCards: list[tuple[set[int], set[int]]] = []
    winning = set()
    have = set()
    for card in cards:
        w, h = card.split('|')
        w = set(int(x) for x in w.split(':')[1].strip().split())
        h = set(int(x) for x in h.strip().split())
        parsedCards.append((w, h))
    return parsedCards

def partOne():
    cards = load_file()
    parsedCards = parseCards(cards)
    total = 0
    for winning, have in parsedCards:
        nWinners = len(winning.intersection(have))
        if nWinners: total += 2 ** (nWinners - 1)
    print(total)

def partTwo():
    cards = load_file()
    parsedCards = parseCards(cards)
    nCards = [1] * len(parsedCards)
    for idx, (winning, have) in enumerate(parsedCards):
        nWinners = len(winning.intersection(have))
        for i in range(idx+1,idx+1+nWinners):
            if i < len(nCards): nCards[i] += nCards[idx]
    print(sum(nCards))

if __name__ == '__main__':
    if sys.argv[1] == '1':
        partOne()
    elif sys.argv[1] == '2':
        partTwo()