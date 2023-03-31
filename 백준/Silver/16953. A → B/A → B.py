from collections import deque

start, end = map(int, input().split(' '))

dx = [2, '1']

def bfs(start):
    q = deque()
    q.append([start, 1])
    
    while q:
        x, depth = q.popleft()
        
        if x == end:
            return depth

        for i in range(2):
            if i == 0:
                nx = x * dx[i]
            else:
                nx = int(str(x) + dx[i])

            if nx <= end:
                q.append([nx, depth+1])
    return -1
                
print(bfs(start))