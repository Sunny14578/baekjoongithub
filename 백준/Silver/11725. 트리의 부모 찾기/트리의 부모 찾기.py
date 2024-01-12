from collections import deque


n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visit = [0]*(n+1)

def bfs():
    q = deque([1])
    
    while q:
        val = q.popleft()
 
        for i in graph[val]:
            if visit[i] == 0:
                visit[i] = val
                q.append(i)
bfs()

for i in range(2, len(visit)):
    print(visit[i])