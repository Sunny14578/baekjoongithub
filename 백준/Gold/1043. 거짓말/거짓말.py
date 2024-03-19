def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a in true and b in true:
        return
    
    if a in true:
        parent[b] = a    
    elif b in true:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
n, m = map(int, input().split())
true = list(map(int, input().split()))[1:]

parent = list(range(n+1))
party = []

for _ in range(m):
    p = list(map(int, input().split()))
    p = p[1:]
        
    for i in range(len(p)-1):
        union(p[i], p[i+1])
    
    party.append(p)
    
answer = 0
    
for i in party:
    for j in range(len(i)):
        if find(parent, i[j]) in true:
            break
    else:
        answer += 1

print(answer)