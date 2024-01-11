from collections import deque

n, m, start = list(map(int, input().split(' ')))

arr = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split(' '))
    arr[u].append(v)
    arr[v].append(u)

graph = [sorted(e) for e in arr]

visit = [0]*(n+1)

def bfs(x):
    Q = deque()
    Q.append(x)
    
    while Q:
        x = Q.popleft()
        visit[x] = 1
        print(x, end = ' ')
        
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = 1
                Q.append(i)

visit2 = [0]*(n+1)

def dfs(x):
    visit2[x] = 1
    print(x, end = ' ')
    for i in graph[x]:
        if visit2[i] == 0:
            visit2[i] = 1
            dfs(i)
    
dfs(start)
print()
bfs(start)

