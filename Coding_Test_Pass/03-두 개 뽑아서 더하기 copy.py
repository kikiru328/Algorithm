# 권장시간: 30분
# 권장 시간 복잡도: O(NlogN)

"""
정수 배열 numbers 가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아
반환하는 solution() 함수를 완성하세요

- 제약조건
    - numbers의 길이는 2이상 100이하
    - numbers의 모든 수는 0이상 10 이하
    
- 입출력 예
[2, 1, 3, 4, 1] -> [2, 3, 4, 5, 6, 7]
[5, 0, 2, 7] -> [2, 5, 7, 9, 12]
"""

# 입력값: 정수 배열을 받는다
def solution(arr):
    result = []
    # 서로 다른 2개의 수를 뽑는다.
    for i in range(len(arr)): # 우선 하나를 뽑는다.
        for j in range(i+1, len(arr)): # 뽑은거 제외 나머지를 순환한다.
    # 더한값을 추가한다.
            result.append(arr[i] + arr[j])
    # 만들 수 있는 모든 수 -> 집합
    result = set(result)
    # 오름차순 정렬
    result = sorted(result) # 정렬 + list
    return result

# test
print(solution([2,1,3,4,1]))

