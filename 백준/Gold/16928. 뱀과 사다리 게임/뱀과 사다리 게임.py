n, m = map(int, input().split(' '))

n_list = []
m_list = []

for i in range(n):
    n_list.append(list(map(int, input().split(' '))))
    
for j in range(m):
    m_list.append(list(map(int, input().split(' '))))
    
visit = [0]*101
arr= [i for i in range(101)]

for i in n_list:
    a, b = i
    
    arr[a] = b
    
for j in m_list:
    a, b = j
    
    arr[a] = b    
    
from collections import deque

dx = [1, 2, 3, 4, 5, 6]

def bfs(x):
    q = deque()
    q.append([x, 0])
    visit[x] = 1
    
    while q:
        x, depth = q.popleft()
        
        if x == 100:
            return depth
        
        for i in range(6):
            nx = x + dx[i]
            
            if nx < 101 and visit[nx] == 0:
                q.append([arr[nx], depth+1])
                visit[nx] = 1
                
print(bfs(1))