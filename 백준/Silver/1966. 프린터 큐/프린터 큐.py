from collections import deque

n = int(input())

for i in range(n):
    cnt = 1
    
    q_n, index = map(int, input().split())
    q_value = map(int, input().split())
    q = deque([(i, idx) for idx, i in enumerate(q_value)])
    
    MIN = min(q)
    
    while q:
        if q[0][0] == max(i[0] for i in q):
            if q[0][1] == index:
                print(cnt)
                break
            else:
                q.popleft()
                cnt += 1
        else:
            q.rotate(-1)