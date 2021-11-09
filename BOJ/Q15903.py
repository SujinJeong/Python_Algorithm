from queue import PriorityQueue

pq = PriorityQueue()

n, m = map(int, input().split())
# 1차원 배열 입력받기
list = list(map(int, input().split()))

for i in range(0, n):
    pq.put(list[i])

while m != 0:
    num1 = pq.get()
    num2 = pq.get()

    total = num1 + num2

    pq.put(total)
    pq.put(total)

    m -= 1

answer = 0
while True:
    if pq.empty():
        break

    answer += pq.get()

print(answer)

