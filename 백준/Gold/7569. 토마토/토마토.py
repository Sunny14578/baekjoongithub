m, n, t = map(int, input().split())

arr = []

for j in range(t):
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split(' '))))
    arr.append(temp)

    
def check():
    boolean = True
    
    for i in range(t):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    boolean = False

    return boolean


from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():

    q = deque()
    
    for i in range(t):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    q.append([i, j, k, 0])
    
    if len(q) == 0:
        return 0
    
    while q:
        z, x, y, d = q.popleft()
        
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if 0 <= nz < t and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny] == 0:
                
                arr[nz][nx][ny] = 1
                q.append([nz, nx, ny, d+1])
    return d



if check():
    print(0)
else:
    result = bfs()
    
    if check():
        print(result)
    else:
        print(-1)