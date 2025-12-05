import sys
from collections import defaultdict
from itertools import combinations

graph = defaultdict(list)

for line in sys.stdin.readlines():
    a, b = line.strip().split("-")
    graph[a].append(b)
    graph[b].append(a)

counts = defaultdict(int)

for k, v in graph.items():
    for x, y in combinations(v, 2):
        counts[frozenset([k, x, y])] += 1


part1 = 0
for s, count in counts.items():
    if count > 1 and any(l.startswith("t") for l in s):
        part1 += 1

print(part1)
