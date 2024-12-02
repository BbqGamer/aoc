{
    split($0, a) 
    for (i = 1; i <= length(a); i++) {
        new_list = ""
        for (j = 1; j <= length(a); j++) {
            if (i != j) {
                new_list = new_list " " a[j]
            }
        }
        print NR new_list
    }
}
