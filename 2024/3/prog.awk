$1 == "do"   { disabled = 0 }
$1 == "dont" { disabled = 1 }
$1 == "mul"  {
    if (disabled) next
    res += $2 * $3
}
END { print res }

