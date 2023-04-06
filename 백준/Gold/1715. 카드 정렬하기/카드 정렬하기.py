import heapq

n = int(input())

arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))
    
s = 0

if len(arr)==1:
    print(s)
else:
    for i in range(n-1): # 2개씩 꺼내기 떄문에 n-1
        previous = heapq.heappop(arr)
        current = heapq.heappop(arr)

        s += previous + current
        heapq.heappush(arr, previous + current)
    
    print(s)