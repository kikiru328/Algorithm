import itertools
N, M = map(int, input().split())
cards = list(map(int, input().split()))

comb = list(itertools.combinations(cards, 3))
total = 0
for i in comb:
    if sum(i) <= M:
        total = max(total, sum(i)) # 더 큰 값
print(total)
