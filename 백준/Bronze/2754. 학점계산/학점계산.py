w = input()
score = 0

def major_score(w):
    if "A" in w:
        return 4
    elif "B" in w:
        return 3
    elif "C" in w:
        return 2
    elif "D" in w:
        return 1
    else:
        return 0

def detail_score(w):
    if '+' in w:
        return 0.3
    elif '-' in w:
        return -0.3
    else:
        return 0

score += major_score(w)
score += detail_score(w)
print(float(score))
