m = int(input())

arr = []

for i in range(m):
    arr.append(list(map(int, input().rstrip())))
    
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    arr[x][y] = 0
    cnt = 1
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < m and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                Q.append([nx, ny])
                cnt+=1
    return cnt

result = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            result.append(bfs(i, j))
            

result.sort()
print(len(result))
for k in result:
    print(k)