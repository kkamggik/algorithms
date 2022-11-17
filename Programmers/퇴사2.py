n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    t = i + arr[i][0]
    if( t <= n ):
        dp[i] = max(dp[i+1], dp[t] + arr[i][1])
    else:
        dp[i] = dp[i+1]
print(max(dp))