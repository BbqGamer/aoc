import sys

data = [l.strip() for l in sys.stdin.readlines()]
to_visit = {(i, j) for i in range(len(data)) for j in range(len(data[i]))}


def out_of_bound(i, j):
    return i < 0 or j < 0 or i >= len(data) or j >= len(data[0])


def neighborbood(i, j):
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        yield i + di, j + dj


def dfs(i, j):
    area = 1
    peri = 0
    for ni, nj in neighborbood(i, j):
        if out_of_bound(ni, nj) or data[ni][nj] != data[i][j]:
            peri += 1
            continue

        if (ni, nj) in to_visit:
            to_visit.remove((ni, nj))
            narea, nperi = dfs(ni, nj)
            area += narea
            peri += nperi

    return area, peri


result = 0
while to_visit:
    i, j = to_visit.pop()
    area, perimeter = dfs(i, j)
    result += area * perimeter

print(result)
