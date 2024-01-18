import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    
    arr.append([a, b])

arr.sort()

answer = [arr[0][1]]
heapq.heapify(answer)

for i in range(1, len(arr)):
    if answer[0] <= arr[i][0]:
        heapq.heappop(answer)
    heapq.heappush(answer, arr[i][1])

print(len(answer))