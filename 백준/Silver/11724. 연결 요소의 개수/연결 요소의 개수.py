m, n = map(int, input().split(' '))

graph = [[]*i for i in range(m+1)]

for i in range(1, n+1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    

from collections import deque

visit = [0]*(m+1)

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1 
    
    while q:
        n = q.popleft()
        
        for i in graph[n]:
            nx = i
            
            if visit[nx] == 0:
                q.append(nx)
                visit[nx] = 1
    return 1

result = 0

for i in range(1, m+1):
    if visit[i] == 0:
        result += bfs(i)
        
print(result)