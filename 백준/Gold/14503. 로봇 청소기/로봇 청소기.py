import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []

for _ in range(n):
    v = list(map(int, input().split()))
    graph.append(v)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]      

cnt = 1
graph[x][y] = -1
    
while graph[x][y] != 1:
    flag = 1
        
    for _ in range(4):
        d -= 1
        
        if d == -1:
            d = 3
        
        nx = x + dx[d]   
        ny = y + dy[d]
 
        if graph[nx][ny] == 0:
            x, y = nx, ny
            graph[x][y] = -1
            cnt += 1
            flag = 0
            break
                    
    if flag == 1:
        x += dx[d-2]
        y += dy[d-2]
        
print(cnt)