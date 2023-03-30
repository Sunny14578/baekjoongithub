from collections import deque

start, end = map(int, input().split(' '))

visit = [0]*200001

dx = [2, -1, 1]

def bfs():
    q = deque()
    q.append([start, 0])
    visit[start] = 1
    
    while q:
        x, time = q.popleft()
        
        if x == end:
            return time
        
        for i in range(3):
            if i == 0:
                nx = x * dx[i]
                
                if visit[nx] == 0 and 0 <= nx <= 100000:
                    q.append([nx, time])
                    visit[nx] = 1
            else:
                nx = x + dx[i]
                
                if visit[nx] == 0 and 0 <= nx <= 100000:
                    q.append([nx, time+1])
                    visit[nx] = 1
print(bfs())