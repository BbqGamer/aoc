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


def cheated_neighbors(cur, dist=2):
    i, j = cur
    for x in range(i - dist, i + dist + 1):
        for y in range(j - dist, j + dist + 1):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue

            steps = abs(x - i) + abs(y - j)
            if steps <= dist and grid[x][y] != "#":
                yield x, y, steps


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

    for part, CHEAT_STEPS in enumerate([2, 20]):
        cheat_count = 0

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "#":
                    continue

                for x, y, steps in cheated_neighbors((i, j), CHEAT_STEPS):
                    if distances[(x, y)] - distances[(i, j)] - steps >= 100:
                        cheat_count += 1

        print(f"Part {part + 1}: {cheat_count}")
