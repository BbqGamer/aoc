def expand(arr):
    new = []
    for num in arr:
        snum = str(num)
        if num == 0:
            new.append(1)
        elif len(snum) % 2 == 0:
            half = len(snum) // 2
            l = int(snum[:half])
            r = int(snum[half:])
            new.append(l)
            new.append(r)
        else:
            new.append(num * 2024)
    return new


def part1(starting):
    cur = starting
    for _ in range(25):
        cur = expand(cur)
    return len(cur)


EXAMPLE = [125, 17]


def test_expand():
    res_1 = expand(EXAMPLE)
    assert res_1 == [253000, 1, 7]
    res_2 = expand(res_1)
    assert res_2 == [253, 0, 2024, 14168]
    res_3 = expand(res_2)
    assert res_3 == [512072, 1, 20, 24, 28676032]


def test_part1():
    cur = EXAMPLE
    res = part1(cur)
    assert res == 55312


if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(part1(data))
