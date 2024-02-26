import sys
sys.setrecursionlimit(10**6)


n, r, q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

def dfs(v):
    visit[v] += 1

    for i in graph[v]:
        if visit[i] == 0:
            visit[v] += dfs(i)
 
    return visit[v]

for i in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    
    graph[u].append(v)
    graph[v].append(u)
      
dfs(r)

for _ in range(q):
    print(visit[int(sys.stdin.readline())])