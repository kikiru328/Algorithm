def fac(x):
    s = 1
    for i in range(1, x+1):
        s *= i
    return s

t = int(input())
print(fac(t))