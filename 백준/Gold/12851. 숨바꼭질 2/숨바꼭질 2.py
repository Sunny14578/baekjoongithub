from collections import deque

start, end = map(int, input().split(' '))

visit = [0] * 100001 

dx = [-1, 1, 2]

cnt = 0
def bfs(start):
    global cnt
    q = deque()
    q.append([start, 0])
    visit[start] = 0
    
    while q:
        x, depth = q.popleft()
        
        if x == end:
            cnt += 1
            continue
          
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]

            if 0 <= nx < 100001 and (visit[x]+1 == visit[nx] or visit[nx] == 0):
                q.append([nx, depth + 1])
                visit[nx] = depth+1

bfs(start)

print(visit[end])
print(cnt)