from itertools import accumulate

disk = list(map(int, input()))
offsets = list(accumulate([0] + disk))[:-1]

D = list(zip(disk, offsets))

full = D[::2]
empty = D[1::2]

checksum = 0
for identifier in reversed(range(len(full))):
    moved = False
    n, offset = full[identifier]
    for i in range(len(empty)):
        en, eoffset = empty.pop(i)
        if offset <= eoffset:
            break

        if n > en:
            empty.insert(i, (en, eoffset))
            continue

        checksum += ((n * (n - 1)) // 2 + eoffset * n) * identifier
        diff = en - n
        if diff:
            empty.insert(i, (diff, eoffset + n))
        moved = True
        break
    if not moved:
        checksum += ((n * (n - 1)) // 2 + offset * n) * identifier


print(checksum)
