import sys

part1 = 0
for line in sys.stdin:
    best = 0
    for l, a in enumerate(line[:-1]):
        for r, b in enumerate(line[l + 1:]):
            num = int(a + b)
            if num > best:
                best = num
    part1 += best
print(part1)
                





