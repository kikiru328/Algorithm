def rcp(x,y):
    if x == y:
        print("비겼습니다")
    if (x=="가위") and (y=="바위"):
        print("바위가 이겼습니다!")
    elif (x=="바위") and (y=="보"):
        print("보가 이겼습니다!")
    elif (x=="보") and (y=="가위"):
        print("가위가 이겼습니다!")
a = input()
b = input()
x = input()
y = input()
rcp(x,y)