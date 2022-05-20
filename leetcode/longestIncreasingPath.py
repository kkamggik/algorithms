class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x,y,val):
            if not(0<=x<m and 0<=y<n) or matrix[y][x]<=val: return 0
            if dp[y][x]!=-1: return dp[y][x]
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                dp[y][x] = max(dp[y][x], dfs(nx,ny,matrix[y][x]))
            dp[y][x]+=1
            return dp[y][x]
        res = -1
        n,m = len(matrix), len(matrix[0])
        dirc = [[0,1],[0,-1],[1,0],[-1,0]]
        dp = [[-1]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(j,i,-1))
        return res
    