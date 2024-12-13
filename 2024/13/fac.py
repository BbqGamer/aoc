import re
import sys

import numpy as np

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

    A = np.array([[xa, xb], [ya, yb]], dtype=np.int64)
    b = np.array([xd, yd], dtype=np.int64)
    resa, resb = np.round(np.linalg.solve(A, b))
    if resa * xa + resb * xb == xd and resa * ya + resb * yb == yd:
        print(int(resa), int(resb))
        part2 += 3 * resa + resb

print(part2)
