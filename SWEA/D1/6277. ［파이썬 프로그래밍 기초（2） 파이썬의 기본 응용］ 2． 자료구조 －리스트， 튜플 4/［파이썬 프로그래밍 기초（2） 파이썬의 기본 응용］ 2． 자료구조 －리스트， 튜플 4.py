L = []
for i in range(5):
    L.append(int(input()))
print(f"입력된 값 {L}의 평균은 {round( sum(L) / 5, 1)}입니다.")