import sys

import graphviz


def dfs(node, G):
    if node == "out":
        return 1

    return sum(dfs(e, G) for e in G[node])


if __name__ == "__main__":
    G = {}
    dot = graphviz.Digraph()
    for line in sys.stdin:
        node, r = line.strip().split(": ")
        dot.node(node)
        edges = r.split()
        for e in edges:
            dot.edge(node, e)
        G[node] = set(edges)

    dot.render("res.gv", view=True)
    print(dfs("you", G))
