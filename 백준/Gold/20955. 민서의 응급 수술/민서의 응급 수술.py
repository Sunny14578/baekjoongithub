import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, a, b):
    
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]

cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    
    if find(parent, u) == find(parent, v):
        cnt += 1
        
    union(parent, u, v)
    

for i in range(1, n):
    if find(parent, i) != find(parent, i+1):
        union(parent,i,i+1)
        cnt += 1
        
print(cnt)