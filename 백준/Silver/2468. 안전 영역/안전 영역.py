from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = []
MAX = 0

for i in range(n):
    l = list(map(int, input().split()))
    MAX = max(max(l), MAX)
    
    graph.append(l)
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

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
                visit[nx][ny] = 1
                q.append([nx, ny])
                
answer = 1

for d in range(1, MAX+1):
    visit = [[0]  *n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= d:
                visit[i][j] = 1
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    
    answer = max(cnt, answer)
    
print(answer)