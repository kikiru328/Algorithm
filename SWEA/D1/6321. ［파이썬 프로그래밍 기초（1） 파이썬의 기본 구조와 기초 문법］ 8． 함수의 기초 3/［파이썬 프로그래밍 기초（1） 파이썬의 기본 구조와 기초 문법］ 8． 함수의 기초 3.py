import math
N = int(input())

def is_prime(N):
    if N != 1:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                break
        else:
            print("소수입니다.")
is_prime(N)