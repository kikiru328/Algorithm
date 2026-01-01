# 정수 배열을 하나 받습니다. 배열의 중복값을 제거하고 배열 데이터를 내림차순으로 정렬하여 반환하는 solution() 함수를 구현하세요.
# 배열 길이는 2이상 100,000이하입니다.
# 각 배열의 데이터 값은 -100,000 이상 100,000 이하입니다.
# 권장시간 복잡도: O(NlogN)


def solution(arr):
    return sorted(list(set(arr)), reverse=True)


print(solution([4, 2, 2, 1, 3, 4]))
