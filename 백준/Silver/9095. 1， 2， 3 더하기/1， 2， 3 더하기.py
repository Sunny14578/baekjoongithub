from collections import deque

def bfs(x):
    Q = deque([x])
    cnt = 0
    
    while Q:
        number = Q.popleft()

        if number == 0:
            cnt += 1
        else:
            for step in [1, 2, 3]:
                if number - step >= 0:
                    Q.append(number - step)
    return cnt

n = int(input())

for i in range(n):
    start = int(input())
    print(bfs(start))