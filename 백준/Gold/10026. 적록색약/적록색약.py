n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(str, input().rstrip())))
               
from collections import deque

visit = [[0]*n for i in range(n)]
visit2 = [[0]*n for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, check):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and check == arr[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx, ny])

def bfs2(x, y, check):
    q = deque()
    q.append([x, y])
    visit2[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit2[nx][ny] == 0 and check == arr2[nx][ny]:
                visit2[nx][ny] = 1
                q.append([nx, ny])
                
import copy
arr2 = copy.deepcopy(arr)

for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'
            
cnt = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j, arr[i][j])
            cnt += 1
            
        if visit2[i][j] == 0:
            bfs2(i, j, arr2[i][j])
            cnt2 += 1
print(cnt, cnt2)