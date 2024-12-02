function abs(x) { return x < 0 ? -x : x }
function sign(x) { return x < 0 ? -1 : 1 }
{
    split($0, a, " ") 
    direction = sign(a[2] - a[1])
    for (i = 1; i < length(a); i++) {
        diff = a[i+1] - a[i]
        if (sign(diff) != direction) {
            next
        }
        dist = abs(a[i] - a[i+1])
        if (dist < 1 || dist > 3) {
            next
        }
    }
    count++
}
END {
    print count
}

