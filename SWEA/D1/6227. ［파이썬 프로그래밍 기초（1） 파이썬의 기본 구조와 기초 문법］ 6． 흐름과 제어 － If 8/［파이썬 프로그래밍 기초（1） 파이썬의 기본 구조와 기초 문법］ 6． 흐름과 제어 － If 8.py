s = ""
for i in range(100, 301):
    if i % 2 == 0:
        if (int(str(i)[0]) % 2 == 0) and (int(str(i)[1]) % 2 == 0) and (int(str(i)[2]) % 2 == 0):
            s += f"{i},"
print(s[:-1])