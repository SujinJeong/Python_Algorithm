while True:
    # 들어오는 값들을 int로 모두 변환
    a, b = map(int, input().split())
    
    if a == 0 or b == 0:
        break

    if a > b:
        print("Yes")
    else:
        print("No")
