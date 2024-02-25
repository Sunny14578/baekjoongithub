n, m = map(int, input().split())

answer = [0] * (n+1)
for i in range(m):
    s, e, c = map(int, input().split())
    
    for j in range(s, e+1):
        answer[j] = c
        
print(' '.join(map(str, answer[1:])))