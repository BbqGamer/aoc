import itertools
import sys

data = sys.stdin.read().strip().split("\n\n")

WIDTH = 5
HEIGHT = 7

keys, locks = [], []
for d in data:
    arr = d.split("\n")
    counts = [0 for _ in range(WIDTH)]
    for i in range(1, HEIGHT - 1):
        for j in range(WIDTH):
            if arr[i][j] == "#":
                counts[j] += 1

    if arr[0][0] == "#":
        locks.append(tuple(counts))
    else:
        keys.append(tuple(counts))


result = 0
for key, lock in itertools.product(keys, locks):
    sumed = [key[i] + lock[i] for i in range(WIDTH)]
    if all(s <= HEIGHT - 2 for s in sumed):
        result += 1
        continue

print(result)
