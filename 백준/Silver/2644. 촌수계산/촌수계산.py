from collections import deque

n = int(input())
start, finish = map(int, input().split(' '))
cnt = int(input())

arr = [[]*i for i in range(n+1)]

for i in range(cnt):
    a, b = map(int, input().split(' '))
    
    arr[a].append(b)
    arr[b].append(a)

visit = [0]*(n+1)

def bfs():
    q = deque()
    q.append([start, 0])
    
    while q:
        x, depth = q.popleft()
        
        if x == finish:
            return depth
        
        for i in arr[x]:
            if visit[i] == 0:
                q.append([i, depth+1])
                visit[i] = 1
    return -1

print(bfs())