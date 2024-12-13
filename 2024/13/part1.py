import re
import sys
from functools import cache

sys.setrecursionlimit(1500)

PATTERN = (
    r"Button A: X\+(\d+), Y\+(\d+)\n"
    r"Button B: X\+(\d+), Y\+(\d+)\n"
    r"Prize: X=(\d+), Y=(\d+)"
)

res = 0
for x in re.finditer(PATTERN, sys.stdin.read()):
    xa, ya, xb, yb, xd, yd = map(int, x.groups())

    @cache
    def moves(x, y):
        if x == xd and y == yd:
            return 0

        if x > xd or y > yd:
            return float("inf")

        return min(3 + moves(x + xa, y + ya), 1 + moves(x + xb, y + yb))

    m = moves(0, 0)
    if m != float("inf"):
        res += m

print(res)
