m, n = map(int, input().split(' '))

arr = []

for i in range(m):
    arr.append(list(map(int, input().split(' '))))

from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
result = 0

def bfs():
    arr2 = copy.deepcopy(arr)
    q = deque()
    
    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            if arr2[i][j] == 2:
                q.append([i, j])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and arr2[nx][ny] == 0:
                arr2[nx][ny] = 2
                q.append([nx, ny])
                
    global result
    
    cnt = 0
    for i in arr2:
        cnt += i.count(0)

        
    result = max(result, cnt)
    
    
def wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(count+1)
                arr[i][j] = 0
                
wall(0)
print(result)