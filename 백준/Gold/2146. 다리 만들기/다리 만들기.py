from collections import deque

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def number_bfs(x, y, land_cnt):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    arr[x][y] = land_cnt
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] != 0:
                    arr[nx][ny] = land_cnt
                    q.append([nx, ny])
                    visit[nx][ny] = 1

visit = [[0]*n for i in range(n)]

land_cnt = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and visit[i][j] == 0:
            number_bfs(i, j, land_cnt)
            land_cnt += 1    
            
def bfs(cnt):
    visit = [[0]*n for i in range(n)]
    
    q2 = deque()
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == cnt:
                q2.append([i, j, 0])
                
    while q2:
        x, y, depth = q2.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] != cnt and arr[nx][ny] != 0:
                    return depth
                else:
                    q2.append([nx, ny, depth+1]) # 인접한 바다좌표 추가
                    visit[nx][ny] = 1
    return depth

final = 10000

for i in range(1, land_cnt):
    final = min(final, bfs(i))

print(final)