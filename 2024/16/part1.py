import heapq
import sys

VERTICAL = 0
HORIZONTAL = 1

if __name__ == "__main__":
    starting = end = None

    grid = [l.strip() for l in sys.stdin.readlines()]
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                starting = (i, j, HORIZONTAL)
            elif c == "E":
                end = (i, j)

    assert starting is not None
    assert end is not None

    visited = set()
    pq = [(0, starting)]

    while pq:
        dist, (cur_i, cur_j, orientation) = heapq.heappop(pq)
        if (cur_i, cur_j) in visited:
            continue

        if grid[cur_i][cur_j] == "#":
            continue

        if (cur_i, cur_j) == end:
            print("Part 1: ", dist)
            break

        visited.add((cur_i, cur_j))

        horscore = 1
        vertscore = 1001
        if orientation == VERTICAL:
            horscore = 1001
            vertscore = 1

        heapq.heappush(pq, (dist + horscore, (cur_i, cur_j + 1, HORIZONTAL)))
        heapq.heappush(pq, (dist + horscore, (cur_i, cur_j - 1, HORIZONTAL)))
        heapq.heappush(pq, (dist + vertscore, (cur_i + 1, cur_j, VERTICAL)))
        heapq.heappush(pq, (dist + vertscore, (cur_i - 1, cur_j, VERTICAL)))
