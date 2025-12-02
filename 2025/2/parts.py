import sys

data = sys.stdin.read().strip()
ranges = [range.split('-') for range in data.split(",")]

part1 = 0
part2 = 0
for (l, r) in ranges:
    for num in range(int(l), int(r) + 1):
        num_str = str(num)
        num_len = len(num_str)
        for divisor in range(2, num_len + 1):
            if num_len % divisor != 0:
                continue # check if is acutal divisor

            seq_len = num_len // divisor
            seq = num_str[:seq_len]
            for i in range(1, divisor):
                seq_start = seq_len * i
                if num_str[seq_start: seq_start + seq_len] != seq:
                    break
            else:
                if divisor == 2:
                    part1 += num
                part2 += num
                break

print(part1)
print(part2)