import fileinput


def is_valid(target, acc, pos, arr):
    if pos == len(arr):
        return target == acc

    if acc > target:
        return False

    return (
        is_valid(target, acc + arr[pos], pos + 1, arr) or
        is_valid(target, acc * arr[pos], pos + 1, arr) or
        is_valid(target, int(str(acc) + str(arr[pos])), pos + 1, arr)
    )


res = 0
for line in fileinput.input():
    s = line.strip().split()
    num = int(s[0][:-1])
    arr = list(map(int, s[1:]))
    if is_valid(num, arr[0], 1, arr[1:]):
        res += num

print(res)
