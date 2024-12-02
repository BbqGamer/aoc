function abs(x) { return x < 0 ? -x : x }
function sign(x) { return x < 0 ? -1 : 1 }
{
    cur_sign = sign($2 - $1)
    for (i = 1; i < NF; i++) {
        diff = $(i+1) - $(i)
        dist = abs(diff)
        if (sign(diff) != cur_sign || dist < 1 || dist > 3)
            next
    }
    count++
}
END {print count}
