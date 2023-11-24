def solution(triangle):
    
    l = len(triangle)
    dp = [[0]*l for _ in range(l)]
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle)-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
                
    answer = max(dp[-1])
    return answer