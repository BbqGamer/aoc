import sys
from collections import defaultdict
from functools import cache


def solve(st, en, G_inv):
    @cache
    def aux(start, end):
        if start == end:
            return 1
        return sum(aux(start, n) for n in G_inv[end])

    return aux(st, en)


if __name__ == "__main__":
    invG = defaultdict(set)
    for line in sys.stdin:
        node, r = line.strip().split(": ")
        edges = r.split()
        for e in edges:
            invG[e].add(node)

    print(solve("you", "out", invG))

    print(
        solve("svr", "fft", invG)
        * solve("fft", "dac", invG)
        * solve("dac", "out", invG)
    )
