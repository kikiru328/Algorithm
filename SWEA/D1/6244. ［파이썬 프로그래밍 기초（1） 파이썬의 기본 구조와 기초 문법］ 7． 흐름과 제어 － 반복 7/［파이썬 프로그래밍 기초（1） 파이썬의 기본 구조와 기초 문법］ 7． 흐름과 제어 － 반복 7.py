data = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
c = 0 
while data:
    a = data.pop()
    if a >= 80:
        c += a
print(c)