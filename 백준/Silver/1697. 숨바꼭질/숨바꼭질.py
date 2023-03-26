start, end = map(int, input().split(' '))

dx = [-1, 1, 2]

from collections import deque
MAX = 10 ** 5

def bfs(x):
    Q = deque()
    Q.append([x, 0])
    cnt = 0
    visit = [0] * (MAX + 1)
    
    while Q:
        x, depth = Q.popleft()
        
        if x == end:
            return depth
        
        for i in range(3):
            if i == 2:
                nx = x * dx[2]
            else:
                nx = x + dx[i]
            
            if 0 <= nx <= MAX and visit[nx] != 1:
                visit[nx] = 1
                Q.append([nx, depth+1])
            
print(bfs(start))