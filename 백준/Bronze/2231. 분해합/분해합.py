N = int(input())
def solution(N):
    for i in range(max(0, N - 9 * len(str(N))), N):
        num = i + sum(map(int, str(i)))
        if num == N:
            return (i)
    else:
        return(0)
print(solution(N))