import re
import sys

from scipy.optimize import linprog

sys.setrecursionlimit(1500)

PATTERN = (
    r"Button A: X\+(\d+), Y\+(\d+)\n"
    r"Button B: X\+(\d+), Y\+(\d+)\n"
    r"Prize: X=(\d+), Y=(\d+)"
)

part2 = 0
for x in re.finditer(PATTERN, sys.stdin.read()):
    xa, ya, xb, yb, xd, yd = map(int, x.groups())
    xd += 10000000000000
    yd += 10000000000000

    c = [3, 1]
    A = [[xa, xb], [ya, yb]]
    b = [xd, yd]

    integrality = [1, 1]
    res = linprog(c, A_eq=A, b_eq=b, integrality=[3, 3])

    print(res.status)
    if res.status == 0:
        an, bn = map(int, res.x)
        part2 += int(res.fun)


print(part2)
