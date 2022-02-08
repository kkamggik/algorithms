n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    for j in range(coins[i], k+1):
        dp[j] += dp[j-coins[i]]
print(dp[k])