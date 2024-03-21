from collections import deque

def solution(maps):

    visit = [[0] * len(maps[0]) for i in range(len(maps))]

    
    def bfs(start):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        q = deque([[start[0], start[1], 0]])

        while q:
            x, y, depth = q.popleft()

            if x == len(maps)-1 and y == len(maps[0])-1:
                return depth+1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 0:
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        q.append([nx, ny, depth+1])
        return -1
                        
    answer = bfs([0, 0])
    
    return answer


