scores = [88, 30, 61, 55, 95]
def filter(score):
    if score >= 60:
        return "합격"
    else:
        return "불합격"
for i, score in enumerate(scores):
    print(f"{i+1}번 학생은 {score}점으로 {filter(score)}입니다.")
    