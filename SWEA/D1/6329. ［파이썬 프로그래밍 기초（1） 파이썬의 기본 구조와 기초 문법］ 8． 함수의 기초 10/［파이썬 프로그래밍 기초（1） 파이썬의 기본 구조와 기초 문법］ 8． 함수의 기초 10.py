def countdown(x):
    if x <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(x, 0, -1):
            print(i)
            
countdown(0)
countdown(10)