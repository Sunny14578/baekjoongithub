from collections import deque

n, m = map(int, input().split(' '))

arr = []

for i in range(m):
    c = list(map(int, input().split(' ')))
    arr.append(c)
    
Q = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            Q.append([i, j])
            


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
      
            
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
              
                arr[nx][ny] = arr[x][y]+1
                Q.append([nx, ny])
                
bfs()

result = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
    result = max(result, max(arr[i]))
print(result-1)