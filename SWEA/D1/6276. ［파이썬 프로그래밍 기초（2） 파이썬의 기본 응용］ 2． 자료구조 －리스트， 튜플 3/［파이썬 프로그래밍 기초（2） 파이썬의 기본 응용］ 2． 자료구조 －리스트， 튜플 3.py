x = []
for i in range(2, 10):
    y = []
    for j in range(1, 10):
        if ((i * j) % 3 != 0) and ((i * j) % 7 != 0):
            y.append(i*j)
    x.append(y)
    
print(x)