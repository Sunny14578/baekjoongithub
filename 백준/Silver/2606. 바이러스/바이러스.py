from collections import deque

m = int(input())
n = int(input())

arr = [[] for i in range(m+1)]

for i in range(n):
    i, v = map(int, input().split(' '))
    arr[i].append(v)
    arr[v].append(i)

visit = [0]*(m+1)

def bfs(x):
    Q = deque()
    Q.append(x)
    
    while Q:
        x = Q.popleft()
        
        for i in arr[x]:
            if visit[i] == 0:
                visit[i] = 1
                Q.append(i)
                
    return visit

if m == 1 and n == 0:
    print(0)
else:
    print(sum(bfs(1))-1)