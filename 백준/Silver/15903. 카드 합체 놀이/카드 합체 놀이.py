from heapq import heapify, heappush, heappop

n, m = map(int, input().split(' '))
number = list(map(int, input().split(' ')))
heapify(number)

for i in range(m):
    plus = heappop(number) + heappop(number)

    heappush(number, plus)
    heappush(number, plus)
print(sum(number))