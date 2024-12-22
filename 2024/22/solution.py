import sys

res = 0
for line in sys.stdin.readlines():
    num = int(line)
    for _ in range(2000):
        num = num ^ (num << 6)
        num %= 16777216

        num = num ^ (num >> 5)
        num %= 16777216

        num = num ^ (num << 11)
        num %= 16777216

    res += num
print(res)
