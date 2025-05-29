# find prime
import math

N: int = int(input())

def eratosthenes_prime(N):
    prime: list = [True] * (N+1)
    prime[0] = prime[1] = False

    for i in range(2, int(math.sqrt(N)+1)):
        if prime[i]: # if true
            for j in range(i*i, N+1, i): # from i*i to N+1 jump by i = multiple
                prime[j] = False # delete multiple
    result: list = []
    for i in range(2, N+1):
        if prime[i]: #0, 1 is not prime
            result.append(str(i))
    print(" ".join(result))

eratosthenes_prime(N)
