n, m = map(int, input().split(' '))

arr = []


for i in range(n):
    arr.append(list(map(int, input().split(' '))))

birus = []
wall = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            birus.append([i, j])
        
        if arr[i][j] == 1:
            wall += 1
            
from itertools import combinations
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(birus):
    global visit, result
    visit = [[-1]*n for _ in range(n)]
    cnt = 0
    q = deque()
    
    for i in birus:
        q.append([i[0], i[1]])
        visit[i[0]][i[1]] = 0
     
    while q:
        x, y  =  q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1 and graph[nx][ny] != 1:
                if graph[nx][ny] == 2:
                    q.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
                    
                elif graph[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
                    cnt = max(cnt, visit[nx][ny])
        
    if sum(visit, []).count(-1)!= wall:
        return 5000  
    return cnt

result = 5000

birus_list = combinations(birus, m)

for i in birus_list:
    graph = copy.deepcopy(arr)
    result = min(result, bfs(i))

print(result if result != 5000 else -1)