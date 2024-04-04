import sys
input = sys.stdin.readline

n = int(input())
a = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(a):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1 # 사과위치 1로 넣기
    
l = int(input())
di = []
for i in range(l):
    c, d = input().split()
    di.append([int(c), d])
    
dx = [0, 1, 0, -1] # 동 남 서 북 90도 씩 회전
dy = [1, 0, -1, 0]

x = 0
y = 0
cnt = 0
k = 0

q = []

while True:
    
    if k == -1:
        k = 3
    elif k == 4:
        k = 0

    nx = x + dx[k]
    ny = y + dy[k]
    
    if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] == 2:
        break 
    
    cnt += 1
    
    if graph[nx][ny] == 1:
        graph[x][y] = 2
        if [x, y] not in q:
            q.append([x, y])
    else:
        if q:
            lx, ly = q.pop(0)
            graph[lx][ly] = 0

    graph[nx][ny] = 2
    q.append([nx, ny])
        
    x, y = nx, ny # 현재 위치 갱신
    
    if di:
        if di[0][0] == cnt:
            if di[0][1] == 'D':
                k += 1       
            else:
                k -= 1
            di.pop(0)

print(cnt+1)