T = input()
print("".join([w for ind, w in enumerate(T) if ind%2==0]))