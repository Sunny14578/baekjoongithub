import heapq
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(files)
    
    answer = 0
    
    while len(files) > 1:
        value = heapq.heappop(files) + heapq.heappop(files)
   
        heapq.heappush(files, value)
        
        answer += value
        
    print(answer)