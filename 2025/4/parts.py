import sys

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

prev = start = np.array([[c == "@" for c in line.strip()] for line in sys.stdin])
part1 = False
while True:
    s = sliding_window_view(np.pad(prev, (1, 1)), (3, 3))
    cur = (s[:, :, 1, 1] == 1) & (s.sum(axis=(2, 3)) > 4)
    if not part1:
        part1 = True
        print("part1:", np.sum(start) - np.sum(cur))
    if np.all(cur == prev):
        break
    prev = cur

print("part2: ", np.sum(start) - np.sum(cur))
