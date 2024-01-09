n = int(input())

start = []
exit = []

for i in range(n*2):
    s = input()
    
    if i < n:
        start.append([i, s])
    else:
        for k in start:
            if k[1] == s:
                exit.append([k[0], s])

cnt = 0
answer = 0

for i in range(len(exit)):
    for j in range(i+1, len(exit)):
        if exit[i] > exit[j]:
            answer += 1
            break
print(answer)