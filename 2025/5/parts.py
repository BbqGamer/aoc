import sys


class Ranges:
    ranges = []

    def __init__(self, data: str):
        for line in data.split():
            left, right = map(int, line.split("-"))
            self._add_range(left, right)

    def _add_range(self, left, right):
        i = 0
        while True:
            if i >= len(self.ranges):
                break
            rl, rr = self.ranges[i]
            if rl <= left and rr >= right:
                return

            if rr >= left and rr <= right:
                if rl < left:
                    left = rl
                self.ranges.pop(i)
                continue

            if rl >= left and rl <= right:
                if rr > right:
                    right = rr
                self.ranges.pop(i)
                continue
            i += 1

        self.ranges.append((left, right))

    def __len__(self):
        return sum(right - left + 1 for left, right in self.ranges)

    def __contains__(self, item):
        return any(item >= left and item <= right for (left, right) in self.ranges)


if __name__ == "__main__":
    data = sys.stdin.read()
    first, second = data.split("\n\n")
    ranges = Ranges(first)
    part1 = sum(int(item) in ranges for item in second.split())
    print("part1:", part1)
    print("part2:", len(ranges))
