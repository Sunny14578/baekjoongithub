r, c, t = map(int, input().split())

arr = []
air = []

for i in range(r):
    li = list(map(int, input().split()))
    
    if -1 in li:         # 공기청정기 위치를 저장하기 위한 코드
        air.append(i)
    arr.append(li)
    
def spread():
    # 새로운 배열을 만들고 공기청정기 위치를 적용하는 코드
    new_arr = [[0] * c for _ in range(r)]     

    for a in air:
        new_arr[a][0] = -1
    
    # 우, 좌, 하, 상 으로 인접한 4방향을 체크하기 위한 코드
    dx = [1, -1, 0, 0]        
    dy = [0, 0, 1, -1]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] >= 0: # 미세먼지가 존재하는지 체크
                new_arr[i][j] += arr[i][j] # 존재하면 새 배열에 먼지 값 더해주기
                
                for d in range(4): # 우좌하상 체크 후 좌표 업데이트
                    nx = i + dx[d]
                    ny = j + dy[d]
                    
                    # 배열의 길이와 공기청정기가 없는곳만 탐색하기 위한 조건
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        new_arr[nx][ny] += arr[i][j]//5
                        new_arr[i][j] -= arr[i][j]//5
    return new_arr

def rotate():
    # 위쪽 반시계
    top = air[0]

    # 맨 왼쪽 열 먼지 정화시키기
    for x in range(top-1, 0, -1):
        arr[x][0] = arr[x-1][0]
    
    # 맨 위쪽 행 먼지 이동하기
    for y in range(c-1):
        arr[0][y] = arr[0][y+1]
        
    # 맨 오른쪽 열 먼지 이동하기
    for x in range(top):
        arr[x][-1] = arr[x+1][-1]
        
    # 공기청정기가 존재하는 행 옮기기
    for y in range(c-1, 0, -1):  
        arr[top][y] = arr[top][y-1]
        

    # 아래쪽 시계
    bottom = air[1]
    
    # 맨 왼쪽 열 먼지 정화시키기
    for x in range(bottom+1, r-1):
        arr[x][0] = arr[x+1][0]
        
    # 맨 아래 행 먼지 옮기기
    for y in range(c-1):
        arr[-1][y] = arr[-1][y+1]
        
    #  맨 오른쪽 열 먼지 옮기기
    for x in range(r-1, bottom, -1):
        arr[x][-1] = arr[x-1][-1] 
        
    # 공기청정기가 존재하는 행 옮기기
    for y in range(c-1, 0, -1):
        arr[bottom][y] = arr[bottom][y-1]
    
    # 공기청정기에서 부터 나온 값 없애주기
    arr[top][1] = 0 
    arr[bottom][1] = 0

for _ in range(t):
    arr = spread()
    rotate()

answer = sum(sum(i) for i in arr) + 2
print(answer)