import heapq, sys

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    number = int(sys.stdin.readline())
    
    if number == 0:
        if heap:
            print(abs(heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap, -number)