res = ""
# first create simple adder
res += "x00 AND y00 -> carry00\n"
res += "x00 XOR y00 -> z00\n"

for i in range(1, 44):
    z = f"z{i-1:02}"
    x, y = f"x{i:02}", f"y{i:02}"
    res += f"{x} AND {y} -> and{i}\n"
    res += f"{x} XOR {y} -> xor{i}\n"
    res += f"xor{i} XOR carry{i-1} -> {z}\n"
    res += f"and{i} AND carry{i-1} -> cand{i}\n"
    res += f"cand{i} OR and{i} -> carry{i}\n"

with open("adder.txt", "w") as f:
    f.write(res)
