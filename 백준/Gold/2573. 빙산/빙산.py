m, n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    visited[x][y] += 1

                if not visited[nx][ny] and arr[nx][ny] != 0 :
                    queue.append([nx,ny])
                    visited[nx][ny] = True


time = 0
while True:
    count = 0
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if not visited[i][k] and arr[i][k]!=0:
                bfs(i,k)
                count +=1

    for i in range(m):
        for k in range(n):
            if visited[i][k] :
                arr[i][k] -= (visited[i][k]-1)
                if arr[i][k] < 0: arr[i][k] = 0

    time += 1
    if count == 0:
        print(0)
        exit()
    if count >=2 :
        break

print(time-1)