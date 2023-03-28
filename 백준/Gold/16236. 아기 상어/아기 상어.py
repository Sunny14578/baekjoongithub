from collections import deque

n = int(input())

arr = []
start = 0

for i in range(n):
    c = list(map(int, input().split(' ')))
    
    if 9 in c:
        start = [i, c.index(9)]
        
    arr.append(c)

# 상 좌 우 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

shark = 2
time = 0
cnt = 0

def bfs(x, y):
    global shark, cnt
    
    visit = [[0]*n for i in range(n)]
    
    l1 = [] 
    q = deque()
    q.append([x, y])
    arr[x][y] = 0
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        if cnt == shark:
            cnt = 0
            shark += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] <= shark:
                
                if arr[nx][ny] == 0 or arr[nx][ny] == shark:
                    q.append([nx, ny])
                    visit[nx][ny] = visit[x][y]+1
                    
                elif arr[nx][ny] < shark:
                    l1.append([visit[x][y], nx, ny])
                    
           # print(l1)
            
    return sorted(l1, key = lambda x: (x[0], x[1], x[2]))

x, y = start

while True:

    l = deque(bfs(x, y))
    
    if not l:
        break
    
    t, x, y = l.popleft()
    cnt += 1
    time += t
print(time)