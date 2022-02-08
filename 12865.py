n,k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
bags = [[]]
for _ in range(n):
    w,v = map(int, input().split())
    bags.append([w,v])
for i in range(1,n+1):
    for j in range(k+1):
        w,v = bags[i][0], bags[i][1]
        if j < w: dp[i][j] = dp[i-1][j]
        if j >= w: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n][k])
    
 