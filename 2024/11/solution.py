from functools import lru_cache


@lru_cache(maxsize=None)
def solve(number, iters=75):
    if iters == 0:
        return 1

    if number == 0:
        return solve(1, iters - 1)

    snum = str(number)
    if len(snum) % 2 == 0:
        half = len(snum) // 2
        l = int(snum[:half])
        r = int(snum[half:])
        return solve(l, iters - 1) + solve(r, iters - 1)

    return solve(number * 2024, iters - 1)


if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(sum([solve(x, 25) for x in data]))
    print(sum([solve(x) for x in data]))
