import sys

LEN = 12
part2 = 0
for line in sys.stdin:
    best = ''
    index = -1
    for i in range(LEN):
        maximum = '0'
        remaining = LEN - i
        for j in range(index + 1, len(line) - remaining):
            if line[j] > maximum:
                index = j
                maximum = line[j]
                if maximum == '9':
                    break
        best += maximum
    print(best)
    part2 += int(best)
print(part2)
                





