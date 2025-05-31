import sys
inp = sys.stdin.readline
values = [25, 10, 5, 1]
for _ in range(int(inp())):
    remains = int(inp())
    coins = [0, 0, 0, 0]
    for i in range(4):
        coins[i], remains = divmod(remains, values[i])
    print(*coins)