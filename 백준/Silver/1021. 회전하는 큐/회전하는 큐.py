from collections import deque

N, M = map(int, input().split())
num = list(map(int, input().split()))

q = deque(range(1, N+1))

cnt = 0

while num:    
    l = len(q)
    if q[0] == num[0]:
        q.popleft()
        num.pop(0)
     
    elif q.index(num[0]) > l - q.index(num[0]):
        q.rotate()
        cnt += 1
        
    else:
        q.rotate(-1)
        cnt += 1
print(cnt)