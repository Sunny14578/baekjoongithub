from collections import deque


def bfs(start, seven11):
    q = deque()
    q.append(start)
    visit = [0]*n

    while q:
        x, y = q.popleft()
        if abs(end[0] - x) + abs(end[1] - y) <= 1000:
            return 'happy'
        else:
            for i in range(len(seven11)):
                if visit[i] == 0:
                    nx, ny = seven11[i]

                    if abs(nx - x) + abs(ny - y) <= 1000:
                        q.append([nx, ny])
                        visit[i] = 1           
    return 'sad'

t = int(input())

for i in range(t):
    n = int(input())
    start = list(map(int, input().split(' ')))

    seven11 = [] 
    for i in range(n):
        seven11.append(list(map(int, input().split(' '))))
    end = list(map(int, input().split(' ')))
    
    print(bfs(start, seven11))