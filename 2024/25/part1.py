import sys

data = sys.stdin.read().strip().split("\n\n")

keys = [], locks = []
for d in data:
    arr = d.split("\n")
    counts = [0 for _ in range(5)]
    for i in range(7):
        for j in range(5):
            if arr[i][j] == "#":
                counts[j] += 1

    if arr[0][0] == "#":
        locks.append(tuple(counts))
    else:
        keys.append(tuple(counts))
