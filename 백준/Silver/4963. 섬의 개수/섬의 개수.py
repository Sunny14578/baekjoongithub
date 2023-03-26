from collections import deque

# 상 하 좌 우 좌상 좌하 우상 우하
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs():
    q = deque()
    
    cnt= 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append([i, j])
                arr[i][j] = 2

                while q:
                    x, y = q.popleft()

                    for k in range(8):
                        nx = x+dx[k]
                        ny = y+dy[k]

                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                            q.append([nx, ny])
                            arr[nx][ny] = 2

                cnt += 1
    return cnt

result = []

while True:

    m, n = map(int, input().split(' '))
    
    if m == 0 and n == 0:
        break

    arr = []
    
    for i in range(n):
        arr.append(list(map(int, input().split(' '))))
        
    result.append(bfs())

    
for i in result:
    print(i)