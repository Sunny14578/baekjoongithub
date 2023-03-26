# 좌상
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, -2, -1, 2, 1]

def bfs(start):
    x, y = start
    visit[x][y] = 1
    
    q = deque()
    q.append([x, y, 0])
    
    while q:
        x, y, d = q.popleft()
        
        if x == end[0] and y == end[1]:
            return d
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < size and 0 <= ny < size and visit[nx][ny] == 0:
                q.append([nx, ny, d+1])
                visit[nx][ny] = 1
    return d
                
t = int(input())

for k in range(t):
    size = int(input())

    visit = [[0] * size for i in range(size)]

    start = list(map(int, input().split(' ')))
    end = list(map(int, input().split(' ')))
    
    print(bfs(start))