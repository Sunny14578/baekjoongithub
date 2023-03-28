from collections import deque

m, n, c = map(int, input().split(' '))

arr = [[0]*n for i in range(m)]

for i in range(c):
    y1, x1, y2, x2 = map(int, input().split(' '))
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    arr[x][y] = 1
    
    cnt = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                q.append([nx, ny])
                arr[nx][ny] = 1
                cnt += 1
            
    return cnt+1

result = []

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            result.append(bfs(i, j))

result.sort()

print(len(result))

for i in result:
    print(i, end = ' ')