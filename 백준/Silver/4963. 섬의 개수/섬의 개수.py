from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    arr[x][y] = 2

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 2

result = []

while True:

    m, n = map(int, input().split(' '))
    
    if m == 0 and n == 0:
        break

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split(' '))))
        
    # 상 하 좌 우 좌상 좌하 우상 우하
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1]

    
    cnt= 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)