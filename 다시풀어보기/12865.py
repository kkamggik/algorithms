n,k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(k+1):
        w,v  = items[i-1]
        if(j < w): dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])