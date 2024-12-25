import itertools
import sys

data = sys.stdin.read().strip().split("\n\n")

WIDTH = 5
HEIGHT = 7

keys, locks = [], []
for d in data:
    arr = d.strip().split("\n")
    counts = tuple(
        len(list(filter(lambda a: a == "#", col))) for col in list(zip(*arr))
    )
    if arr[0][0] == "#":
        locks.append(counts)
    else:
        keys.append(counts)

result = 0
for key, lock in itertools.product(keys, locks):
    if all(key[i] + lock[i] <= HEIGHT for i in range(len(lock))):
        result += 1

print(result)
