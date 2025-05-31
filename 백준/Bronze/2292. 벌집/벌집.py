n = 1
wall = 1
T = int(input())
while T > n: # wall 내 taret 숫자가 있을 경우
    n +=  6 * wall # 각 wall은 6배수 # 6배수로 증가
    wall += 1 # 6배수 내 없을 경우 wall + 1
print(wall)