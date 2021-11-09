n = int(input())

if n == 1:
    print('')
else:
    # 나눠보기
    for i in range(2, n+1):
        # 반복
        while n % i == 0:
            print(i)
            n = n/i