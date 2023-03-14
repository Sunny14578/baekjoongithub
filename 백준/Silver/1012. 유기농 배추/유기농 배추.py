from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    Q = deque()
    Q.append([x, y])
    arr[x][y] = 0
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1:
                Q.append([nx, ny])
                arr[nx][ny] = 0
                
                
t = int(input())

result = []

for i in range(t):
    m, n, c = map(int, input().split(' '))

    arr = [[0]*(n) for _ in range(m)]

    for i in range(c):
        x, y = map(int, input().split(' '))
        arr[x][y] = 1
    
    cnt = 0

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)