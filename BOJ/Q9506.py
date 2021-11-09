while True:
    num = int(input())

    if num == -1:
        break

    total = 0
    list = []
    # 약수 계산
    for i in range(1, num):
        # 약수이면
        if num % i == 0:
            total += i
            list.append(i)

    if total == num:
        answer = str(num) + " = "
        for i in range(0, len(list)-1):
            answer += str(list[i]) + " + "
        answer += str(list[len(list)-1])

        print(answer)
    else:
        print(num, "is NOT perfect.")