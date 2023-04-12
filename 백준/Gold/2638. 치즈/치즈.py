from collections import deque

m, n = map(int, input().split(' '))

arr = []

for i in range(m):
    arr.append(list(map(int, input().split(' '))))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    
    melt = []
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                else:
                    arr[nx][ny] += 1

hour = 0

while True:
    visit = [[0]*n for _ in range(m)]
    
    bfs(0, 0)
    
    melt = []
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] != 0:
                if arr[i][j] >= 3:
                    melt.append([i, j])
                else:
                    arr[i][j] = 1
                
    if len(melt) == 0:
        break
        
    for i in melt:
        x, y = i
        arr[x][y] = 0
        
    hour += 1        

print(hour)