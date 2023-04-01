from collections import deque

T = int(input())

def check(depth):
    if depth%2 == 0:
        return -1
    else:
        return 1

def bfs(x):
    q = deque()
    
    d = 0
    q.append([x, d+1])
    visit[x] = check(d)
    
    while q:
        x, depth = q.popleft()

        for i in graph[x]:
            if visit[i] == 0:
                q.append([i, depth+1])
                visit[i] = check(depth)
            elif visit[i] == check(depth):
                pass
            elif visit[i] != check(depth):
                return False
    return True

final = []

for i in range(T):
    m, n = map(int, input().split(' '))

    graph = [[] for i in range(m+1)]
    visit = [0] * (m+1)
    
    for _ in range(n):
        a, b = map(int, input().split(' '))

        graph[a].append(b)
        graph[b].append(a)
    
    result = []
    for i in range(1, m+1):
        if visit[i] == 0:
            result.append(bfs(i))
    
    if all(result):
        final.append('YES')
    else:
        final.append('NO')
        
for i in final:
    print(i)