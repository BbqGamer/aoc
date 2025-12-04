import sys

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

data = [[True if c == "@" else False for c in line.strip()] for line in sys.stdin]
arr = np.array(data)
total = 0
while True:
    slide = sliding_window_view(np.pad(arr, (1, 1)), (3, 3))
    toremove = (slide[:, :, 1, 1] == 1) & (slide.sum(axis=(2, 3)) <= 4)
    sum_remove = np.sum(toremove)
    if total == 0:
        print("part 1:", sum_remove)
    total += sum_remove
    if sum_remove == 0:
        break
    arr = arr & ~toremove
print("part 2:", total)
