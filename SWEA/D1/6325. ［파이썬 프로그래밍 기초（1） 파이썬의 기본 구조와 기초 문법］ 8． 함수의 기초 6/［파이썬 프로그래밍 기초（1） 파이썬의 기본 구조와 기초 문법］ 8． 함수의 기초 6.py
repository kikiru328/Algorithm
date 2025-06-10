L = [2, 4, 6, 8, 10]
def find_item(x, L):
    if x in L:
        return f"{x} => True"
    else:
        return f"{x} => False"
print(L)
print(find_item(5, L))
print(find_item(10, L))