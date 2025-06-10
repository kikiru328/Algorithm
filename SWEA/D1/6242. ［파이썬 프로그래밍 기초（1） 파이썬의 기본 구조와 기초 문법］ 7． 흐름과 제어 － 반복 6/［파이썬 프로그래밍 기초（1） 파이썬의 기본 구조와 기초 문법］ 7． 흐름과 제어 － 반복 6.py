data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {}
for bt in data:
    if bt not in result:
        result[bt] = 1
    else:
        result[bt] += 1
print(result)