import sys

import graphviz


def dfs(node, end, G):
    if node == end:
        return 1

    return sum(dfs(e, end, G) for e in G[node])


if __name__ == "__main__":
    G = {}
    dot = graphviz.Digraph()
    for line in sys.stdin:
        node, r = line.strip().split(": ")

        cmap = {
            "dac": "yellow",
            "fft": "yellow",
            "svr": "green",
            "you": "green",
        }
        fillcolor = "white" if node not in cmap else cmap[node]
        dot.node(
            node,
            fillcolor=fillcolor,
            style="filled",
        )
        edges = r.split()
        for e in edges:
            dot.edge(node, e)
        G[node] = set(edges)
    dot.node("out", fillcolor="red", style="filled")

    dot.render("res.gv", view=True)
    print(dfs("you", "out", G))
