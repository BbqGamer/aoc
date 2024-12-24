import sys
from graphlib import TopologicalSorter

a, b = sys.stdin.read().strip().split("\n\n")

values = {}
for line in a.split("\n"):
    k, v = line.split(": ")
    values[k] = int(v)

gates = {}
for line in b.split("\n"):
    a, b = line.split(" -> ")
    gates[b] = a

graph = {}
for out, gate in gates.items():
    s = gate.split()
    graph[out] = {s[0], s[2]}

ts = TopologicalSorter(graph)

for node in ts.static_order():
    if node in values:
        continue

    gate = gates[node]
    d1, op, d2 = gate.split()
    if op == "AND":
        values[node] = values[d1] & values[d2]
    elif op == "OR":
        values[node] = values[d1] | values[d2]
    else:
        values[node] = values[d1] ^ values[d2]

result = ""
for node, val in sorted(values.items(), reverse=True):
    if node.startswith("z"):
        result += str(val)

print(int(result, 2))
