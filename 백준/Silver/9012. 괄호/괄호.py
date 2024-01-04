from collections import deque

n = int(input())

for i in range(n):
    s = input()
    q = deque()
    
    for j in s:
        if q and q[-1] == '(' and j == ')':
            q.pop()
            continue
        q.append(j)
        
    if q:
        print('NO')
    else:
        print('YES')