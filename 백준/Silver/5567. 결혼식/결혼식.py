n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visit = [0] * (n+1)
visit[1] = 1

def dfs(x, depth):
    if depth == 2:
        return 
        
    for i in graph[x]:
        if visit[i] == 0:
            visit[i] = 1
        dfs(i, depth+1)
        
dfs(1, 0)
print(sum(visit)-1)