# 수포자는 수학을 포기한 사람을 줄인 표현이다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려고한다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍는다.
# 1번: 1,2,3,4,5,1,2,3,4,5, ...
# 2번: 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5, ...
# 3번: 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answer가 주어졌을 떄, 가장 많은 문제를 맞힌 사람이
# 누구인지 배열에 담아 반환하도록 solution() 함수를 작성하세요.
# 제약조건 1: 시험은 최대 10,000 문제로 구성되어 있음.
# 제약조건 2: 문제의 정답은 1,2,3,4,5 중 하나
# 제약조건 3: 가장 높은 점수를 받은 사람이 여럿이라면 반환하는 값을 오름차순으로 정렬하세요.
# 입출력 예: answer [1,2,3,4,5] -> return [1]
# 입출력 에: answer [1,3,2,4,2] -> return [1,2,3]
# 권장 시간 복잡도: O(N)


def solution(answers):
    PATTERNS = [
        [1, 2, 3, 4, 5],  # 1
        [2, 1, 2, 3, 2, 4, 2, 5],  # 2
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],  # 3
    ]

    scores = [0] * 3

    # answer를 하나씩 순회하면서
    # 각 패턴에 대해서 평가하면 됨.
    # 패턴은 순회해야 하니까, index 활용 필요.
    # answer의 idx 15라면,
    # 1: 15 % 5(pattern 수) => pattern 0번째.
    # 2: 15 % 8 => pattern 8번째.
    # 3: 15 % 10 => pattern 6번째.

    for idx, answer in enumerate(answers):
        for j, pattern in enumerate(PATTERNS):
            if answer == pattern[idx % len(pattern)]:
                scores[j] += 1

    max_score = max(scores)

    highest_score = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest_score.append(i + 1)

    highest_score.sort()

    return highest_score


assert solution([1, 2, 3, 4, 5]) == [1]
assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]
assert solution([1, 4, 1, 5]) == [1, 3]
