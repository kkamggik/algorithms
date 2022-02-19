import sys
input = sys.stdin.readline
n,m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1e9]*(m+1)
dp[0] = 0
for coin in coins:
    for j in range(1,m+1):
        if j-coin >= 0:
            dp[j] = min(dp[j-coin]+1, dp[j])
if dp[m]==1e9: print(-1)
else: print(dp[m])