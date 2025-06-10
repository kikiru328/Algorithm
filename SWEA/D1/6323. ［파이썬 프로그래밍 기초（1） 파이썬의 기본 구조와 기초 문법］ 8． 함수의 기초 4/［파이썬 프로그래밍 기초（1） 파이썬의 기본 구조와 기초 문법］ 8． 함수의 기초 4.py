def pivo(x):
    p = [1, 1]
    for i in range(2, x):
        p.append(p[i-1] + p[i-2])
    print(p)
        
pivo(10)