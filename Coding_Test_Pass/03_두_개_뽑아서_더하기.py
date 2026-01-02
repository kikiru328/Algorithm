# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 반환하는 solution() 함수를 완성하세요.
# 제약 조건 1: numbers의 길이는 2이상 100이하입니다.
# 제약 조건 2: numbers의 모든 수는 0이상 100이하입니다.
# 입출력: numbers [2,1,3,4,1] -> result [2,3,4,5,6,7]
# 입출력: numbers [5,0,2,7] -> result [2,5,7,9,12]
# 권장 시간 복잡도 O(N^2log(N^2))


def solution(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result.append(arr[i] + arr[j])
    result = sorted(set(result))
    return result


assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
assert solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12]
