from collections import deque
import copy

m, n = map(int, input().split(' '))

arr = []

red = 0
blue = 0
end = 0

for i in range(m):
    c = list(map(str, input().rstrip()))
    
    if 'B' in c:
        blue = [i, c.index('B')]
    if 'R' in c:
        red = [i, c.index('R')]
    if 'O' in c:
        end = [i, c.index('O')]
        
    arr.append(c)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = []

def bfs():
    q = deque()
    q.append([red[0], red[1], blue[0], blue[1], 1])
    visit.append([red[0], red[1], blue[0], blue[1]])
      
    while q:
        rx, ry, bx, by, depth = q.popleft()
        
        if depth > 10:
            return -1
        
        for i in range(4):         # 상하좌우로 기울이는 부분
            nrx, nry, nbx, nby, check = move(rx, ry, bx, by, i)  # move 함수를 통해 기울였을때의 빨강 파랑 좌표 반환
            
            if [nrx, nry, nbx, nby] not in visit:
                if check < 2:
                    q.append([nrx, nry, nbx, nby, depth+1])
                    visit.append([nrx, nry, nbx, nby])
                               
            if check == 1:
                return depth
        
    return -1
    
def move(rx, ry, bx, by, d):
    
    check = 0
    check2 = 0
    final = 0
    
    nrx = rx
    nry = ry
    nbx = bx
    nby = by
    
    while True:
        
        nrx += dx[d]
        nry += dy[d]
   
        if 0 <= nrx < m and 0 <= nry < n:
            if arr[nrx][nry] != '#':
                if arr[nrx][nry] == 'O':            
                    check = 1
            else:
                nrx -= dx[d]
                nry -= dy[d]
                break
                
    while True:
        nbx += dx[d]
        nby += dy[d]
        
        if 0 <= nbx < m and 0 <= nby < n:
            if arr[nbx][nby] != '#':
                if arr[nbx][nby] == 'O':
                    check2 = 1
            else:
                nbx -= dx[d]
                nby -= dy[d]
                break
                
    if nrx == nbx and nry == nby:
        if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
            nrx -= dx[d]
            nry -= dy[d]
        else:
            nbx -= dx[d]
            nby -= dy[d]
            
    if check == 0 and check2 == 1:
        final = 3
    elif check == 1 and check2 == 1:
        final = 2
    elif check == 1 and check2 == 0:
        final = 1
    else:
        final = 0
    
    return nrx, nry, nbx, nby, final
    

print(bfs())