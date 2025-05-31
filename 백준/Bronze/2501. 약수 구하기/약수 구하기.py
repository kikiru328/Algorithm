a, b= map(int, input().split())
def yaksu(x):
    r = []
    for i in range(1, int((x ** 0.5) +1)):
        if x % i == 0:
            r.append(i)
            if i < x//i:
                r.append(x//i)        
    return sorted(r)
        
if len(yaksu(a)) >= b:
    print(yaksu(a)[b-1])
else:
    print(0)