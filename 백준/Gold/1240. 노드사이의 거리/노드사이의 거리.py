from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

def bfs(x, goal, distance):
    q = deque([[x, distance]])
    
    while q:
        v, dis = q.popleft()
        visit[v] = dis
        
        if v == goal:
            break
        
        for i in graph[v]:
            if visit[i[0]] == -1:
                q.append([i[0], i[1]+dis])

for i in range(n-1):
    v, e, dis = list(map(int, input().split())) 
    graph[v].append([e, dis])
    graph[e].append([v, dis])
    
for k in range(m):
    visit = [-1] * (n+1)
    
    v, e = map(int, input().split())
    bfs(v, e, 0)
    
    print(visit[e])

