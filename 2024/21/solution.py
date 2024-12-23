import sys
from functools import cache
from itertools import pairwise

ARROW_KEYPAD = [" ^A", "<v>"]
NUMBER_KEYPAD = ["789", "456", "123", " 0A"]
ARROW_PAD = {"<": (1, 0), "v": (1, 1), ">": (1, 2), "^": (0, 1), "A": (0, 2)}
NUM_PAD = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

pads = [ARROW_KEYPAD] * 25 + [NUMBER_KEYPAD]

MOVES = {
    "^": (-1, 0),
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
}


def neighbors(i, j, r):
    p = pads[r]
    for move, (di, dj) in MOVES.items():
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= len(p) or nj >= len(p[0]) or p[ni][nj] == " ":
            continue
        yield move, ni, nj


@cache
def cost(start, end, level):
    i1, j1 = start
    i2, j2 = end
    if level == 0:
        return abs(i1 - i2) + abs(j1 - j2) + 1

    queue = [(i1, j1, [])]
    visited = set()
    paths = []
    while queue:
        i1, j1, moves = queue.pop(0)
        visited.add((i1, j1))
        if (i1, j1) == (i2, j2):
            paths.append(moves)

        for move, i, j in neighbors(i1, j1, level):
            if (i, j) in visited:
                continue
            queue.append((i, j, moves.copy() + [move]))

    costs = []
    for path in paths:
        length = 0
        for a, b in pairwise(["A"] + path + ["A"]):
            length += cost(ARROW_PAD[a], ARROW_PAD[b], level - 1)
        costs.append(length)
    return min(costs)


if __name__ == "__main__":
    part2 = 0
    for line in sys.stdin.readlines():
        code = line.strip()
        res = 0
        for a, b in pairwise("A" + code):
            num_moves = cost(NUM_PAD[a], NUM_PAD[b], 25)
            res += num_moves
        part2 += res * int(code[:-1])
    print(part2)
