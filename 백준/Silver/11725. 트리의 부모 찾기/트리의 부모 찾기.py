from collections import deque

n = int(input())

arr = [[]*i for i in range(n+1)]

for i in range(1, n):
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

visit = [0]*(n+1)

def bfs():
    q = deque()
    q.append(1)
    
    while q:
        l = q.popleft()
        
        for i in arr[l]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = l
                
bfs()

for i in range(2, len(visit)):
    print(visit[i])