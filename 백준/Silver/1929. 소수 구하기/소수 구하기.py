start, end = map(int, input().split(' '))

visit = [0] * (end+1)

for i in range(2, end+1):   # n번
    visit[i] = 1
    
for i in range(2, end+1):   
    if visit[i] == 1:
        for j in range(i+i, end+1, i):
            visit[j] = 0

for i in range(len(visit)):
    if visit[i] == 1 and i >= start:
        print(i)