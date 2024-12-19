import sys

END = "$"


def parse(data: str):
    towels, desired = data.split("\n\n")
    towels = towels.split(", ")
    desired = desired.split("\n")

    trie = dict()
    for towel in towels:
        cur = trie
        for c in towel:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]
        cur[END] = None

    return trie, desired


if __name__ == "__main__":
    trie, desired = parse(sys.stdin.read().strip())

    cache = dict()

    def backtracking(cur, string):
        cache_id = (id(cur), string)
        if cache_id in cache:
            return cache[cache_id]

        if not string:
            if END in cur:
                return 1
            return 0

        c = string[0]
        res = 0

        if END in cur and c in trie:
            res += backtracking(trie[c], string[1:])

        if c in cur:
            res += backtracking(cur[c], string[1:])

        cache[cache_id] = res
        return res

    part1 = 0
    part2 = 0
    for string in desired:
        res = backtracking(trie, string)
        if res:
            part1 += 1
            part2 += res

    print("Part 1: ", part1)
    print("Part 2: ", part2)
