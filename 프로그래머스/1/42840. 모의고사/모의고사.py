def solution(answers):
    patterns= [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    scores = [0] * 3

    for i, answer in enumerate(answers):  # O(N)
        for j, pattern in enumerate(patterns):  # O(1): 3 상수
            if answer == pattern[i % len(pattern)]:  # 나머지, pattern 순열
                scores[j] += 1
    max_score: int = max(scores)

    highest_scores: list[int] = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i + 1)
    return highest_scores


assert solution([1, 2, 3, 4, 5]) == [1]
assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]