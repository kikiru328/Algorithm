digits = {}
for i in range(0, 10):
    digits[str(i)] = 0
a = input()
for i in a:
    if i in digits:
        digits[i] += 1
print("0 1 2 3 4 5 6 7 8 9")
s = ""
for i in range(0, 10):
    s += f"{digits[str(i)]} "
print(s[:-1])