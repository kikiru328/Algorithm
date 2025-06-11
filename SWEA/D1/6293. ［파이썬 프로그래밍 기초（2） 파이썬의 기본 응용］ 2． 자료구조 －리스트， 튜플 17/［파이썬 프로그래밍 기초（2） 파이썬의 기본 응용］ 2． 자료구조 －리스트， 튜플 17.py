import math

t = list(map(int, input().split(',')))
s = []
for i in t:
    s.append(round(2 * math.pi * i,2))
print(", ".join([str(i) for i in s]))