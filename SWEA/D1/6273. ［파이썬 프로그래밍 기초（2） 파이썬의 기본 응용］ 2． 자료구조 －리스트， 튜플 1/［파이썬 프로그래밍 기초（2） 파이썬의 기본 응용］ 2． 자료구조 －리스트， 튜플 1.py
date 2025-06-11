s = [(90, 80), (85,75), (90,100)]
for ind, score in enumerate(s):
    print(f"{ind+1}번 학생의 총점은 {sum(score)}점이고, 평균은 {round( sum(score) / 2, 1)}입니다.")
    