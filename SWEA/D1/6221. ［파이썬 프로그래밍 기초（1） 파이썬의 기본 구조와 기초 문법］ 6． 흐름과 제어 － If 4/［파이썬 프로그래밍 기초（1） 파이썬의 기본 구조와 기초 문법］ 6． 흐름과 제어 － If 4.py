m1 = input()
m2 = input()
def rsp(m1, m2):
    if m1 == m2:
        return "Result : Draw"
    elif (m1 == "가위" and m2 == "보") or (m1 == "바위" and m2 == "가위") or (m1 == "보" and m2 == "바위"):
        return "Result : Man1 Win!"
    else:
        return "Result : Man2 Win!"
print(rsp(m1, m2))