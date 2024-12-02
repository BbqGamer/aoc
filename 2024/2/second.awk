function abs(x) { return x < 0 ? -x : x }
function sign(x) { return x < 0 ? -1 : 1 }
{
    split($0, a, " ") 
    for (i = 1; i <= length(a); i++) {
        new_list = ""
        for (j = 1; j <= length(a); j++) {
            if (i != j) {
                new_list = new_list " " a[j]
            }
        }
        split(new_list, b, " ")

        direction = sign(b[2] - b[1])
        for (j = 1; j < length(b); j++) {
            diff = b[j+1] - b[j]
            if (sign(diff) != direction) {
                break
            }
            dist = abs(b[j] - b[j+1])
            if (dist < 1 || dist > 3) {
                break
            }
        }
        if (j == length(b)) {
            count += 1
            next
        }
    }
}
END {
    print count
}


