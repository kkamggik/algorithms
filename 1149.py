n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
for i in range(3):
    dp[0][i] = houses[0][i]
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+houses[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+houses[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+houses[i][2]
print(min(dp[n-1]))