import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
dp = [0]*(n+1)
for i in range(n-1,-1,-1):
    dp[i] = dp[i+1]
    if i+arr[i][0]<=n:
        dp[i] = max(dp[i],arr[i][1]+dp[i+arr[i][0]])
print(dp[0])