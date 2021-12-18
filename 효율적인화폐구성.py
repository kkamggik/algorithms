n,m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [2e9]*(m+1)
dp[0] = 0
for i in range(n):
    for j in range(coins[i],m+1):
        if dp[j-coins[i]] != 2e9:
            dp[j] = min(dp[j], dp[j-coins[i]] + 1)
if dp[m]==2e9:
    print(-1)
else:
    print(dp[m])
