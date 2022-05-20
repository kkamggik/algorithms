class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        def dfs(x,y):
            if x==m-1 and y==n-1: return 1
            if dp[y][x]==-1:
                dp[y][x] = 0
                cnt = 0
                for d in dirc:
                    nx,ny = x+d[0],y+d[1]
                    if 0<=nx<m and 0<=ny<n and obstacleGrid[ny][nx]==0:
                        cnt += dfs(nx,ny)
                dp[y][x] = cnt
            return dp[y][x]
        n,m = len(obstacleGrid), len(obstacleGrid[0])
        dirc = [[0,1],[1,0]]
        dp = [[-1]*m for _ in range(n)]
        if obstacleGrid[0][0]==1 or obstacleGrid[n-1][m-1]==1: return 0
        return dfs(0,0)