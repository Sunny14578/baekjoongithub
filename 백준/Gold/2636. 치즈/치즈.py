from collections import deque

m, n = map(int, input().split(' '))

arr = []

for i in range(m):
    arr.append(list(map(int, input().split(' '))))

visit = [[0]*n for i in range(m)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0])
    visit[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    
                if arr[nx][ny] == 1:
                    melt.append([nx, ny])
                    
result = []
cnt = 0

while True:
    visit = [[0]*n for i in range(m)]
    melt = []
    zero_cnt = 0
    
    bfs()
    
    for i in arr:
        zero_cnt += i.count(1)
    
    result.append(zero_cnt)
        
    for i in melt:
        x, y = i
        arr[x][y] = 0
        
    if len(melt) == 0:
        break
        
    cnt+=1
        
print(cnt)
print(result[-2])