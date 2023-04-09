from collections import deque

m, n = map(int, input().split(' '))

arr = []

for i in range(m):
    arr.append(list(map(str, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visit = [[0]*n for i in range(m)]
    
    q = deque()
    q.append([x, y, 0])
    visit[x][y] = 1
    
    while q:
        x, y, depth = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] == 'L':
                q.append([nx, ny, depth + 1])
                visit[nx][ny] = 1
    return depth

MAX = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 'L':
            MAX = max(MAX, bfs(i, j))
print(MAX)