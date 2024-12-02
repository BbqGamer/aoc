{
    for (i = 1; i <= NF; i++) {
        new_list = ""
        for (j = 1; j <= NF; j++) {
            if (i == j) continue
            new_list = new_list " " $j
        }
        print NR new_list
    }
}
