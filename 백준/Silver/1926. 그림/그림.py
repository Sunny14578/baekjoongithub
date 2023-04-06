from collections import deque

m, n = map(int, input().split(' '))

arr = []

for i in range(m):
    arr.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    arr[x][y] = 0
    cnt = 1
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0
                cnt += 1
    return cnt

s = 0
cnt2 = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            s = max(bfs(i, j), s)
            cnt2 += 1

print(cnt2)
print(s)