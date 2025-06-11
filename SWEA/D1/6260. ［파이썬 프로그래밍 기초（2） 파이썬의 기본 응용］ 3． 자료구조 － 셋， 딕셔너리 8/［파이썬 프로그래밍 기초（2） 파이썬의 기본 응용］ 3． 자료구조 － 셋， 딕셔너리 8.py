T = input()
x = [ w for w in T if w.isalpha()==True]
up, lo = 0, 0
for w in x:
    if w.isupper():
        up+=1
    else: lo+=1
print(f"UPPER CASE {up}")
print(f"LOWER CASE {lo}")