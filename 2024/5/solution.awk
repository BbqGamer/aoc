BEGIN { FS = "|" }
/\|/  { dependencies[$2][$1] = 1 }
/^$/  { FS = "," } 
/,/ {
    delete present; delete dep_count; delete order

    # which pages are present in current line?
    for(i = 1; i <= NF; i++) {
        present[$i] = 1
    }

    # count dependencies
    for(page in present) {
        dep_count[page] = 0  # initialize even pages without deps
        for(dep in dependencies[page]) {
            if(dep in present) {
                dep_count[page] += 1
            }
        }
    }

    # topological sort (by page_counts)
    for(page in dep_count) {
        order[dep_count[page]] = page
    }

    # check if current set of pages is sorted correctly
    invalid = 0
    for(v in order) {
        if (order[v] != $(v+1)) {
            invalid = 1
            break
        }
    }
    mid = int(length(order) / 2)
    if (invalid) {
        part2 += order[mid]
    } else {
        part1 += order[mid]
    }
}
END {
    print "Part 1:", part1
    print "Part 2:", part2
}

