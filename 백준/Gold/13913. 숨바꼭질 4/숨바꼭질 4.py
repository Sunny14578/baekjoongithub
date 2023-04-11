from collections import deque

start, end = map(int, input().split(' '))

visit = [0] * 10**8 

dx = [-1, 1, 2]

q2 = deque()

def bfs(start):
    q = deque()
    q.append([start, 0])
    visit[start] = 1
    
    while q:
        x, depth = q.popleft()
        
        if x == end:
            return depth
        
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
                
            if 0 <= nx < 100001 and visit[nx] == 0:
                q.append([nx, depth + 1])
                visit[nx] = 1
                q2.append([x, nx, depth+1])
                
print(bfs(start))

result = []
q2.reverse()
check = end

while q2:
    pre, x2, depth = q2.popleft()
    
    if x2 == check:
        result.append(x2)
        check = pre
result.append(start)

result.reverse()
for i in result:
    print(i, end = ' ')