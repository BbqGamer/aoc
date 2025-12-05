import heapq
from itertools import accumulate

disk = list(map(int, input()))
offsets = list(accumulate([0] + disk))[:-1]
D = list(zip(disk, offsets))
full = D[::2]
empty = D[1::2]

index = []
for i in range(10):
    index.append([])

for n, eoffset in empty:
    heapq.heappush(index[n], eoffset)

checksum = 0
for identifier in reversed(range(len(full))):
    moved = False
    n, offset = full[identifier]

    leftmost = float("inf")
    chosen = None
    for en in range(n, len(index)):
        if index[en] and index[en][0] < leftmost and offset > index[en][0]:
            leftmost = index[en][0]
            chosen = en

    if not chosen:
        checksum += ((n * (n - 1)) // 2 + offset * n) * identifier
        continue

    eoffset = heapq.heappop(index[chosen])
    checksum += ((n * (n - 1)) // 2 + eoffset * n) * identifier
    diff = chosen - n
    if diff:
        heapq.heappush(index[diff], eoffset + n)
    moved = True

print(checksum)
