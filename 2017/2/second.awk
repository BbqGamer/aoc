{
    split($0, a)
    for (i = 1; i <= length(a); i++) {
        for(j = 1; j <= length(a); j++) {
            if (i == j) { continue }
            div = a[i] / a[j]
            if (div == int(div)) { 
                res += div
                next
            }
        }
    }
}
END {
    print res
}
