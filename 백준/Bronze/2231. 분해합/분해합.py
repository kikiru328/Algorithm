N = int(input())
def solution(N):
    for i in range(1, N+1):
        num = i + sum(map(int, str(i)))
        if num == N:
            return (i)
    else:
        return(0)
print(solution(N))