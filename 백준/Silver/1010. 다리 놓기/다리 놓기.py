import sys
input = sys.stdin.readline

def solve(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, m+1):
        dp[1][i] = i
    
    for i in range(2, n+1):
        for j in range(i, m+1):
#             dp[2][4] += dp[1][3]
#             dp[2][4] += dp[1][2] 
#             dp[2][4] += dp[1][1]
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]
                
    return dp[n][m]

T = int(input())
for i in range(T):
    n, m  = map(int, input().split())
    print(solve(n, m))