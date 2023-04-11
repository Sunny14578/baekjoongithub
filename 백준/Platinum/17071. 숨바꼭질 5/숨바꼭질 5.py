from collections import deque

start, end = map(int, input().split(' '))

visit = [[-1 for _ in range(500001)] for _ in range(2)]

dx = [-1, 1, 2]


def bfs(start):
    q = deque()
    q.append([start, 0])
    visit[0][start] = 0
    
    while q:
        x, c = q.popleft()
        
        check = c%2
        
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            
            if 0 <= nx < 500001 and visit[1-check][nx] == -1:
                q.append([nx, c+1])
                visit[1-check][nx] = c+1

bfs(start)

t = 0
flag = 0
res = -1
while end <= 500000:
    if visit[flag][end] != -1:
        if visit[flag][end] <= t:
            res = t
            break
    flag = 1 - flag
    t += 1
    end += t
    
print(res)