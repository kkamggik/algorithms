n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for x in range(1, n+1):
    for j in range(n-1, 0, -1):
        if(arr[j+1]<x):
            dp[x][j] = dp[x][j+1] + 1  
        else: 
            dp[x][j] = dp[x][j+1]
ans = 0
for i in range(1,n):
    for j in range(i+1, n+1):
        if(arr[i] < arr[j]): ans += dp[arr[i]][j]
print(ans)