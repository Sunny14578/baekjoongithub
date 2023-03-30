from collections import deque

N, L, R = map(int, input().split(' '))

arr = []

for i in range(N):
    arr.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    
    q = deque()
    q.append([x, y])
    
    check = []
    check.append([x, y])
     
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    check.append([nx, ny])
    return check

result = 0

while True:

    visit = [[0]*N for i in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                c = bfs(i, j)

                if len(c) > 1:
                    flag = 1

                    po = sum([arr[x][y] for x, y in c]) // len(c)

                    for x, y in c:
                        arr[x][y] = po
                
    if flag == 0:
        break
    
    result += 1
    
print(result)