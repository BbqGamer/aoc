import sys

import networkx as nx

G = nx.Graph()
for l in sys.stdin.readlines():
    a, b = l.strip().split("-")
    G.add_edge(a, b)

print(",".join(sorted(max(nx.find_cliques(G), key=lambda c: len(c)))))
