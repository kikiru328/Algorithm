t = list(map(int, input().split(',')))
j = [i for i in t if i%2 !=0]
print(", ".join((str(i) for i in j)))