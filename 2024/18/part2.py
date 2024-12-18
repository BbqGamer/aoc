import heapq
import sys
from collections import defaultdict

BYTES = 1024
SIZE = 71


def neighborhood(i, j, byte_positions):
    N = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
    for x, y in N:
        if (x, y) in byte_positions or x < 0 or y < 0 or x >= SIZE or y >= SIZE:
            continue
        yield (x, y)


if __name__ == "__main__":
    starting = end = None

    byte_positions = set()
    for i, line in enumerate(sys.stdin.readlines()):
        print(i)
        byte_positions.add(tuple(map(int, line.split(","))))

        visited = set()
        distances = defaultdict(lambda: float("inf"))

        pq = [(0, (0, 0))]
        while pq:
            dist, cur = heapq.heappop(pq)
            cur_i, cur_j = cur

            if dist > distances[cur]:
                continue

            distances[cur] = dist

            if cur in visited:
                continue

            if cur == (SIZE - 1, SIZE - 1):
                break

            visited.add(cur)

            for n in neighborhood(cur_i, cur_j, byte_positions):
                if n in visited:
                    continue
                x, y = n
                newdist = dist + 1
                heapq.heappush(pq, (newdist, n))

        if distances[(SIZE - 1, SIZE - 1)] == float("inf"):
            print("Part 2: ", i, line)
            break
