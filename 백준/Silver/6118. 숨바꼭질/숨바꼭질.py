from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(1, m+1):
    a, b = list(map(int, input().split()))
    
    graph[a].append(b)
    graph[b].append(a)

visit = [-1]*(n+1)

def bfs(graph, x, depth):
    q = deque([[x, depth]])
    visit[x] = depth
    
    while q:
        v, d = q.popleft()
        
        for i in graph[v]:
            if visit[i] == -1:
                q.append([i, d+1])
                visit[i] = d+1
        
bfs(graph, 1, 0)

answer = max(visit)

print(visit.index(answer), answer, visit.count(answer))