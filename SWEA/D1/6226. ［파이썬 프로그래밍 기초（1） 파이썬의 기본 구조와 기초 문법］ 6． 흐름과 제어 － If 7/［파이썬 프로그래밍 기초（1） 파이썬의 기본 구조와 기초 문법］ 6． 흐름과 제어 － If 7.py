s = ""
for i in range(1, 201):
    if i % 7 == 0:
        if i % 5 != 0:
            s += f"{i},"
print(s[:-1])