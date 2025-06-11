T = input()
d = {k:0 for k in set(T)}
for w in T:
    d[w] +=1
for k in d:
    print(f"{k},{d[k]}")
        