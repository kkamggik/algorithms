def dfs(x,y):
    if x==n-1 and y==n-1: return 1
    if dp[y][x]==-1:
        dp[y][x] = 0
        x1,y1 = x+arr[y][x],y
        x2,y2 = x,y+arr[y][x]
        if 0<=x1<n and 0<=y1<n: dp[y][x] += dfs(x1,y1) 
        if 0<=x2<n and 0<=y2<n: dp[y][x] += dfs(x2,y2)
    return dp[y][x] 
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
print(dfs(0,0))