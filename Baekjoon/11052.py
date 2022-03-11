n = int(input())
cards = [0]+list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i > j: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-i]+cards[i])
print(dp[n][n])