disk = list(map(int, input()))

left = 0
right = len(disk) - 1

full = True
offset = 0
checksum = 0

while left <= right:
    n = disk[left]
    if full:
        multiplier = (n * (n - 1)) / 2 + offset * n

        checksum += multiplier * (left // 2)
        offset += n
        left += 1
        full = False
    else:
        last_n = disk[right]
        to_put = min(disk[right], n)
        disk[left] -= to_put
        disk[right] -= to_put

        multiplier = (to_put * (to_put - 1)) / 2 + offset * to_put
        checksum += multiplier * (right // 2)

        offset += to_put
        if disk[right] == 0:
            right -= 2
        if disk[left] == 0:
            left += 1
            full = True

print(checksum)
