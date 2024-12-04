BEGIN {FS = ""}
{
    print $0
    for (i = 1; i <= NF; i++) {
        cols[i][NR] = $i
        diag[i - NR][NR] = $i
        diagx[NF - i - NR + 1][NR] = $i
    }
}
END {
    for (i = 1; i <= length(cols); i++) {
        for (j in cols[i]) {
            printf cols[i][j]
        }
        printf "\n"
    }

    for (i in diag) {
        for (j in diag[i]) {
            printf diag[i][j]
        }
        printf "\n"
    }

    for (i in diagx) {
        for (j in diagx[i]) {
            printf diagx[i][j]
        }
        printf "\n"
    }
}
