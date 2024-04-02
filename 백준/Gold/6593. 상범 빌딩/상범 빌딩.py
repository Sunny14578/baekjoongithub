from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(x, y, z):
    q = deque()
    q.append([x, y, z, 0])
    
    while q:
        x, y, z, depth = q.popleft()
        
        if graph[z][x][y] == 'E':
            return f'Escaped in {depth} minute(s).'
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                if visit[nz][nx][ny] == 1:
                    continue
                    
                if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E' :
                    visit[nz][nx][ny] = 1
                    q.append([nx, ny, nz, depth+1])
    return 'Trapped!' 

while True:
    l, r, c = map(int, input().split())
    
    if l == 0 and r == 0 and c == 0:
        break    
        
    visit = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    
    graph = []
    
    for i in range(l):
        
        v1 = []
        
        for j in range(r):
            v2 = list(input())
            
            if 'S' in v2:
                start = [j, v2.index('S'), i]
            
            v1.append(v2)
        input()   
            
        graph.append(v1)
        
    print(bfs(start[0], start[1], start[2]))