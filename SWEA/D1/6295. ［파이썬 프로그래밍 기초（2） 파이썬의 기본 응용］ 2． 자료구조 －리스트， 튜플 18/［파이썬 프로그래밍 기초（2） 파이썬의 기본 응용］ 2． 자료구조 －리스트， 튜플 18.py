row, column = map(int, input().split(','))
print([ [i * j for i in range(column)] for j in range(row)])