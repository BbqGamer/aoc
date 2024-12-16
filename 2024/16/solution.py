import heapq
import sys
from collections import defaultdict

VERTICAL = 0
HORIZONTAL = 1


def neighborhood(i, j, grid):
    N = [
        (i + 1, j, VERTICAL),
        (i - 1, j, VERTICAL),
        (i, j - 1, HORIZONTAL),
        (i, j + 1, HORIZONTAL),
    ]

    for x, y, o in N:
        if grid[x][y] != "#":
            yield x, y, o


if __name__ == "__main__":
    starting = end = None

    grid = [line.strip() for line in sys.stdin.readlines()]
    dist_grid = [list(row) for row in grid]

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                starting = (i, j, HORIZONTAL)
            elif c == "E":
                end = (i, j)

    assert starting is not None
    assert end is not None

    visited = set()
    distances = defaultdict(lambda: float("inf"))
    prevs = defaultdict(lambda: list())

    pq = [(0, starting, None)]
    while pq:
        dist, cur, prev = heapq.heappop(pq)
        cur_i, cur_j, cur_ori = cur

        if dist > distances[cur]:
            continue

        prevs[cur].append(prev)
        distances[cur] = dist

        if cur in visited:
            continue

        visited.add(cur)

        for n in neighborhood(cur_i, cur_j, grid):
            if n in visited:
                continue
            x, y, ori = n
            newdist = dist + 1
            if ori != cur_ori:
                newdist += 1000
            heapq.heappush(pq, (newdist, n, cur))

    visited = set()
    part2 = set()

    def dfs(cur):
        if cur in visited or cur is None:
            return
        visited.add(cur)
        part2.add(cur[:2])
        for prev in prevs[cur]:
            dfs(prev)

    h_end = distances[*end, HORIZONTAL]
    v_end = distances[*end, VERTICAL]

    if h_end < v_end:
        print("Part 1:", h_end)
        dfs((*end, HORIZONTAL))
    elif h_end > v_end:
        print("Part 1:", v_end)
        dfs((*end, VERTICAL))
    else:
        dfs((*end, HORIZONTAL))
        dfs((*end, VERTICAL))

    print(len(part2))
