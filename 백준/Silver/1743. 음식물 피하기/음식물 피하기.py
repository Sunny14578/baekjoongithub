from collections import deque

m, n, k = map(int, input().split(' '))

arr = [[0]*n for i in range(m)]

for i in range(k):
    x, y = map(int, input().split(' '))
    
    arr[x-1][y-1] = 1

visit = [[0]*n for i in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append([nx, ny])
                visit[nx][ny] = 1
                cnt += 1
                
    return cnt

MAX = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            MAX = max(MAX, bfs(i, j))
            
print(MAX)