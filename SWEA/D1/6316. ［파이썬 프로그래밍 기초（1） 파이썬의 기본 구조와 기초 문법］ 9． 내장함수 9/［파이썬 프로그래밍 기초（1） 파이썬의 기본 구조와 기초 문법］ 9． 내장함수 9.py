L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = list(filter(lambda x : x % 2 == 0, L))
s = list(map(lambda x : x ** 2, e ))
print(s)