n = int(input())
Lst = list(map(int, input().split()))
s = 0
def find_yaksu(x):
    return [i for i in range(1, x+1) if x%i ==0]
for x in Lst:
    y = find_yaksu(x)
    if len(y) == 2:
        s+=1
print(s)