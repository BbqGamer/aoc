import sys
from collections import defaultdict

part1 = 0
quaternions_profit_sum = defaultdict(int)

for line in sys.stdin.readlines():
    num = int(line)
    sequence = [num % 10]
    for _ in range(2000):
        num = num ^ (num << 6)
        num %= 16777216

        num = num ^ (num >> 5)
        num %= 16777216

        num = num ^ (num << 11)
        num %= 16777216

        sequence.append(num % 10)
    part1 += num

    diffs = []
    for i in range(len(sequence) - 1):
        diffs.append(sequence[i + 1] - sequence[i])
    sequence.pop(0)

    profits = defaultdict(int)
    for i in range(3, len(diffs)):
        quaternion = tuple(diffs[i - 3 : i + 1])
        profit = sequence[i]
        if quaternion not in profits:
            profits[quaternion] = profit

    for quaternion, profit in profits.items():
        quaternions_profit_sum[quaternion] += profit

print("Part 1: ", part1)
print("Part 2: ", max(quaternions_profit_sum.values()))
