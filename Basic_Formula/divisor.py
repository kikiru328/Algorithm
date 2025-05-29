# find divisor
N: int = int(input())

def find_divisor(N):
    divisors: list = []
    for i in range(1, N+1):
        if N % i == 0: # N divisors
            divisors.append(str(i))
    print(" ".join(divisors))

find_divisor(N)
