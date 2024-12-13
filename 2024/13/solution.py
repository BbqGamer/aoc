import re
import sys

import numpy as np

PATTERN = (
    r"Button A: X\+(\d+), Y\+(\d+)\n"
    r"Button B: X\+(\d+), Y\+(\d+)\n"
    r"Prize: X=(\d+), Y=(\d+)"
)

results = [0, 0]
TO_ADD = [0, 10000000000000]

for x in re.finditer(PATTERN, sys.stdin.read()):
    for i in range(2):
        xa, ya, xb, yb, xd, yd = map(int, x.groups())
        xd += TO_ADD[i]
        yd += TO_ADD[i]

        A = np.array([[xa, xb], [ya, yb]], dtype=np.int64)
        b = np.array([xd, yd], dtype=np.int64)
        resa, resb = np.round(np.linalg.solve(A, b))
        if resa * xa + resb * xb == xd and resa * ya + resb * yb == yd:
            results[i] += 3 * resa + resb

print(int(results[0]))
print(int(results[1]))
