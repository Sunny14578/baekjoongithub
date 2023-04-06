from collections import deque

m, n = map(int, input().split(' '))

arr = []

start = 0
water = []
end = 0

for i in range(m):
    s = list(map(str, input().rstrip()))
    if 'S' in s:
        start = [i, s.index('S')]
    if '*' in s:
        water.append([i, s.index('*')])
    if 'D' in s:
        end = [i, s.index('D')]
    
    arr.append(s)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0]*n for i in range(m)]


def bfs(s, w):
    q = deque()
    
    if len(water) != 0:
        
        for i in water:
            w = [i[0], i[1], -1]   
            q.append(w)    
            visit[i[0]][i[1]] = 1

    
    s = [s[0], s[1], 0]
    q.append(s)
    visit[s[0]][s[1]] = 1        
    
    while q:
        x, y, depth = q.popleft()
        
        if arr[x][y] == 'D':
            return depth
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] != 'X':
                if depth == -1:
                    if nx == end[0] and ny == end[1]:
                        pass
                    else:
                        q.append([nx, ny, -1])
                        visit[nx][ny] = 1                        
                else:
                    q.append([nx, ny, depth + 1])
                    visit[nx][ny] = 1
    return 'KAKTUS'
                    
print(bfs(start, water))