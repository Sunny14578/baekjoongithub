from collections import deque

# 가장 가까운 곳의 먹이가 있는 곳으로 이동한다 (BFS 탐색 활용)
# 너비 깊이만큼이 t초 지났다고 판단

n = int(input())
arr = []
start = 0
for i in range(n):
    li = list(map(int, input().split()))
    
    if 9 in li:
        start = [i, li.index(9)]
    arr.append(li)
    
size = 2
cnt = 0
time = 0

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def bfs(x, y): 
    global cnt, size
    
    visit = [[0] * n for _ in range(n)]
    
    l1 = []
    arr[x][y] = 0 # 상어의 출발위치를 다시 방문할수도 있으므로 0으로 만든다.
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        # 물고기를 먹은수(cnt)와 상어의크기(size)가 같을경우 
        # 상어의 크기를 1늘리고 물고기는 0으로한다.
        if cnt == size: 
            size += 1
            cnt = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 물고기의 크기가 상어보다 같거나 작아야 이동할수 있으므로 조건 추가
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= size and visit[nx][ny] == 0:
                # 물고기의 크기가 같을때는 이동만 할 수 있다.
                if arr[nx][ny] == 0 or arr[nx][ny] == size:
                    q.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1 # 방문할때 마다 1씩 증가시켜서 시간으로 이용한다.
                # 물고기의 크기가 상어보다 작은 경우에 리스트에 해당 (시간, x좌표, y좌표를 추가한다.)
                elif arr[nx][ny] < size:
                    l1.append([visit[x][y], nx, ny])
    
    # 시간을 기준으로 오름차순 정렬하여 가장 가까운 위치를 리턴하게끔한다
    return sorted(l1, key = lambda x: (x[0], x[1], x[2])) 

x, y = start

while True:
    l1 = deque(bfs(x, y))
    
    if not l1:
        break
        
    t, x, y = l1.popleft()
    cnt += 1
    time += t
    
print(time)