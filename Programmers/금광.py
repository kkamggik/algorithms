n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
for i in range(n):
    dp[i][0] = arr[i][0]
for j in range(1,m):
    for i in range(n):
        if i == 0:
            dp[i][j] = max(dp[i][j-1], dp[i+1][j-1])+arr[i][j]
        elif i == (n-1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])+arr[i][j]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1])+arr[i][j]
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])
print(ans)