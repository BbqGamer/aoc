function abs(x) { return x < 0 ? -x : x }
function sign(x) { return x < 0 ? -1 : 1 }
{
    if (done[$1]) next
    cur_sign = sign($(3) - $(2))
    for (i = 2; i < NF; i++) {
        diff = $(i+1) - $(i)
        dist = abs(diff)
        if (sign(diff) != cur_sign || dist < 1 || dist > 3)
            next
    }
    count++
    done[$1] = 1
}
END {
    print count
}
