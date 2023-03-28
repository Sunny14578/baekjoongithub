from collections import deque

m, n = map(int, input().split(' '))

arr = []
for i in range(m):
    arr.append(list(map(int, input().rstrip())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[[0] * 2 for _ in range(n)] for _ in range(m)]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visit[0][0][0] = 1
    
    while q:
        x, y, wall = q.popleft()

        if x == m-1 and y == n-1:
            return visit[x][y][wall]
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny][wall] == 0:
                if arr[nx][ny] == 0:
                    q.append([nx, ny, wall])
                    visit[nx][ny][wall] = visit[x][y][wall]+1
                
                if wall == 0 and arr[nx][ny] == 1:
                    q.append([nx, ny, 1])
                    visit[nx][ny][1] = visit[x][y][wall]+1

    return -1

print(bfs())