from datetime import datetime, date

name = input()
age = int(input())
now = date(2018, 1, 1).year

print("{}(은)는 {}년에 100세가 될 것입니다.".format(name, now-age+101))
