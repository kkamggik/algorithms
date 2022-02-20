import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x,y):
    if x==m-1 and y==n-1: return 1
    if dp[y][x]==-1:
        dp[y][x] = 0
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx] < arr[y][x]:
                dp[y][x] += dfs(nx,ny)
    return dp[y][x]
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
print(dfs(0,0))