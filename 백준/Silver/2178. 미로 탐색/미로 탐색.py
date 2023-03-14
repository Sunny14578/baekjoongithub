from collections import deque

m, n = map(int, input().split())

arr = []
for i in range(m):
    arr.append(list(map(int, input().rstrip())))
    
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append([0, 0])
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y]+1
                Q.append([nx, ny])
               
    return arr[-1][-1]

print(bfs(0, 0))    