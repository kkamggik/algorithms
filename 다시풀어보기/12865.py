n,m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]
bags = []
for _ in range(n):
    w,v = map(int, input().split())
    bags.append([w,v])
for i in range(1,n+1):
    w,v = bags[i-1]
    for j in range(1,m+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n][k])
        