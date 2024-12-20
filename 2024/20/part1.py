import heapq
import sys
from collections import defaultdict


def neighborhood(cur, grid):
    i, j = cur
    N = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]

    for x, y in N:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            continue

        if grid[x][y] != "#":
            yield x, y


def dijkstra(grid):
    visited = set()
    distances = defaultdict(lambda: float("inf"))

    pq = [(0, starting)]
    while pq:
        dist, cur = heapq.heappop(pq)

        if dist > distances[cur]:
            continue

        distances[cur] = dist

        if cur in visited:
            continue

        visited.add(cur)

        for n in neighborhood(cur, grid):
            if n in visited:
                continue
            newdist = dist + 1
            heapq.heappush(pq, (newdist, n))
    return distances


def neighbors_dist_2(cur):
    i, j = cur
    N = [
        (i + 2, j),
        (i - 2, j),
        (i, j - 2),
        (i, j + 2),
        (i + 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j + 1),
    ]
    for x, y in N:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            continue

        if grid[x][y] != "#":
            yield x, y


if __name__ == "__main__":
    starting = end = None

    grid = [list(line.strip()) for line in sys.stdin.readlines()]

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                starting = (i, j)
            elif c == "E":
                end = (i, j)

    assert starting is not None
    assert end is not None

    distances = dijkstra(grid)

    part1 = 0

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c != "#":
                for x, y in neighbors_dist_2((i, j)):
                    if distances[(x, y)] - distances[(i, j)] >= 102:
                        part1 += 1

    print(part1)
