def solution(n):
    
    answer = [[0]*i for i in range(1, n+1)]
    
    row, col = -1, 0
    
    cnt = 1
    
    for i in range(n, 0, -3):
        for j in range(i):
            row+=1
            answer[row][col] = cnt
            cnt+=1

        for j in range(i-1):
            col+=1
            answer[row][col] = cnt
            cnt+=1

        for j in range(i-2):
            row-=1
            col-=1
            answer[row][col] = cnt
            
            cnt+=1


            # [0][0], [1][0], [2][0], [3][0], [4][0] 아래로
            # [4][1], [4][2], [4][3], [4][4] 오른쪽으로
            # [3][3], [2][2], [1][1] # 위로
            # [2][1], [3][1] # 아래로
            # [3][2] # 오른쪽으로

    return [j for i in answer for j in i]