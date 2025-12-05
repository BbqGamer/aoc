import sys

data = [l.strip() for l in sys.stdin.readlines()]
to_visit = {(i, j) for i in range(len(data)) for j in range(len(data[i]))}


def out_of_bound(i, j):
    return i < 0 or j < 0 or i >= len(data) or j >= len(data[0])


N = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def neighborbood(i, j):
    for di, dj in N:
        yield i + di, j + dj


def neighbor_pairs(i, j):
    for x in range(len(N)):
        ai, aj = N[x]
        a = (i + ai, j + aj)

        bi, bj = N[(x + 1) % len(N)]
        b = (i + bi, j + bj)

        diag = (i + ai + bi, j + aj + bj)

        yield a, b, diag


def dfs(i, j):
    area = 1
    peri = 0
    vert = 0
    for (ai, aj), (bi, bj), (di, dj) in neighbor_pairs(i, j):
        aother = out_of_bound(ai, aj) or data[ai][aj] != data[i][j]
        bother = out_of_bound(bi, bj) or data[bi][bj] != data[i][j]
        dother = out_of_bound(di, dj) or data[di][dj] != data[i][j]
        if aother and bother or (not aother and not bother and dother):
            vert += 1

    for ni, nj in neighborbood(i, j):
        if out_of_bound(ni, nj) or data[ni][nj] != data[i][j]:
            peri += 1
            continue

        if (ni, nj) in to_visit:
            to_visit.remove((ni, nj))
            narea, nperi, nvert = dfs(ni, nj)
            area += narea
            peri += nperi
            vert += nvert

    return area, peri, vert


part1 = 0
part2 = 0
while to_visit:
    i, j = to_visit.pop()
    area, peri, vert = dfs(i, j)
    part1 += area * peri
    part2 += area * vert

print(part1)
print(part2)
