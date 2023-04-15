from collections import deque

t = int(input())
m, n = map(int, input().split(' '))

arr = []

for i in range(n):
    arr.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
horse_dx = [ -2, -1, -2, -1, 2, 1, 2, 1]
horse_dy = [-1, -2, 1, 2, -1, -2, 1, 2]

def bfs():
    visit = [[[0]*(t+1) for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0,0])
    visit[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        

      # 목표 지점에 도달하면 return
        if x == n-1 and y == m-1:
            return visit[x][y][z]-1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][z] == 0 and arr[nx][ny] == 0:
                visit[nx][ny][z] = visit[x][y][z]+1
                q.append([nx,ny,z])
                
        if z < t:
            for j in range(8):
                nx = x + horse_dx[j]
                ny = y + horse_dy[j]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 0:
                        if visit[nx][ny][z+1] == 0:
                            visit[nx][ny][z+1] = visit[x][y][z]+1
                            q.append([nx,ny,z+1])
    return -1

print(bfs())