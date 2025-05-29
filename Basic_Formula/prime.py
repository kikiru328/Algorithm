# find prime
import math

N: int = int(input())

def find_prime(N):
    if N == 1:
        print("not prime")
    else:
        for i in range(2, int(math.sqrt(N)+1)):
            if N % i == 0:
                print("not prime")
                break
        else:
            print("prime")

find_prime(N)
