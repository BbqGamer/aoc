import fileinput
from collections import defaultdict
from itertools import combinations

antenas = defaultdict(list)

for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line.strip()):
        if c != ".":
            antenas[c].append(complex(x, y))

antinodes = set()

for frequency, positions in antenas.items():
    for a, b in combinations(positions, 2):
        diff = a - b
        antinodes.add(a + diff)
        antinodes.add(b - diff)


def fits(antinode: complex):
    a = antinode.real
    b = antinode.imag
    return a >= 0 and b >= 0 and a <= x and b <= y


print(len(list(filter(fits, antinodes))))
