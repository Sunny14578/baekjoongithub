from collections import deque

t = int(input())

for i in range(t):
    m, n = map(int, input().split(' '))

    arr = []

    start = 0
    fire = []

    for i in range(n):
        c = list(map(str, input().rstrip()))

        if '@' in c:
            start = [i, c.index('@')]

        arr.append(c)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                fire.append([i, j])
                
    visit = [[0]*m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs():
        q = deque()

        for i in fire:
            x, y = i
            q.append([x, y, -1]) # 불
        q.append([start[0], start[1], 1]) # 사람위치

        while q:
            x, y, depth = q.popleft()

            if x == 0 or x == n-1 or y == 0 or y == m-1:
                if depth != -1:
                    return depth

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and arr[nx][ny] != '*' and arr[nx][ny] != '#':
                    if arr[nx][ny] == '.' and depth == -1:
                        q.append([nx, ny, -1])
                        arr[nx][ny] = '*'
                        visit[nx][ny] = 1


                    if arr[nx][ny] == '.' and depth != -1:
                        q.append([nx, ny, depth+1])
                        visit[nx][ny] = 1

        return 'IMPOSSIBLE'

    print(bfs())