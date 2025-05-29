# find multiple

N: int = int(input())
std: int = int(input())

def find_multiple(N, std):
    multiple: list = []
    for i in range(1, N+1):
        if i % std == 0:
            multiple.append(str(i))
    print(" ".join(multiple))

find_multiple(N, std)
