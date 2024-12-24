import sys

import graphviz

a, b = sys.stdin.read().strip().split("\n\n")

values = {}
for line in a.split("\n"):
    k, v = line.split(": ")
    values[k] = int(v)

gates = {}
for line in b.split("\n"):
    a, b = line.split(" -> ")
    gates[b] = a

dot = graphviz.Digraph()
for out, gate in sorted(gates.items()):
    s = gate.split()
    dot.node(out, label=f"{s[1]} ({out})")
    dot.edge(s[0], out)
    dot.edge(s[2], out)
dot.render("circuit", format="png", cleanup=True)
