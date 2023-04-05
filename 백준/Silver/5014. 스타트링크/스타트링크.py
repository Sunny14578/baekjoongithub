from collections import deque

F, S, G, U, D = map(int, input().split(' '))

dx = [U, -D]

visit = [0] * (F+1)

def bfs():
    q = deque()
    q.append([S, 0])
    visit[S] = 1
    
    while q:
        x, depth = q.popleft()
        
        if x == G:
            return depth
        
        for i in range(2):
            nx = x + dx[i]
            
            if 0 < nx < F+1 and visit[nx] == 0:
                q.append([nx, depth+1])
                visit[nx] = 1
    return 'use the stairs'

print(bfs())