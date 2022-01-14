import sys
input = sys.stdin.readline
tests = int(input())
for t in range(tests):
    n = int(input())
    dp = [[0]*(n+1) for _ in range(2)]
    arr = [list(map(int, input().split())) for _ in range(2)]
    for i in range(n):
        if i%2==0:
            dp[0][i+1] = dp[1][i] + arr[0][i]
            dp[1][i+1] = dp[0][i] + arr[1][i]
        else:
            dp[0][i+1] = dp[1][i] + arr[0][i]
            dp[1][i+1] = dp[0][i] + arr[1][i]
        if i >= 2:
            dp[0][i+1] = max(dp[0][i+1], arr[0][i]+dp[1][i-1])
            dp[1][i+1] = max(dp[1][i+1], arr[1][i]+dp[0][i-1])
    print(max(dp[0][n],dp[1][n]))