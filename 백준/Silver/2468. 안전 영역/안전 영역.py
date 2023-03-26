from collections import deque
import copy

n = int(input())

arr = []
MAX = 0
for i in range(n):
    c = list(map(int, input().split(' ')))
    arr.append(c)
    
    if max(c) >= MAX:
        MAX = max(c)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                q.append([nx, ny])
                visit[nx][ny] = 1

cnt = 1

for d in range(1, MAX+1):
    graph = copy.deepcopy(arr)
    visit = [[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= d:
                visit[i][j] = 1
    cnt2 = 0
    
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                bfs(i, j)
                cnt2 += 1
                
    cnt = max(cnt, cnt2)

print(cnt)                