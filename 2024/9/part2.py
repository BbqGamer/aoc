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

string = ["."] * 65000

checksum = 0
for identifier in reversed(range(len(full))):
    moved = False
    n, offset = full[identifier]
    for en in range(n, len(index)):
        if not index[en]:
            continue

        eoffset = heapq.heappop(index[en])
        if offset < eoffset:
            heapq.heappush(index[en], eoffset)
            continue

        for x in range(eoffset, eoffset + n):
            string[x] = str(identifier)

        checksum += ((n * (n - 1)) // 2 + eoffset * n) * identifier
        diff = en - n
        if diff:
            heapq.heappush(index[diff], eoffset + n)
        moved = True
        break
    if not moved:
        for x in range(offset, offset + n):
            string[x] = str(identifier)
        checksum += ((n * (n - 1)) // 2 + offset * n) * identifier


print("".join(string))

print(checksum)
