class Solution(object):
    def dfs(self,x,y,m,n):
        global dp
        if x==m-1 and y==n-1: return 1
        if dp[y][x]==1e9:
            dp[y][x] = 0
            x1,y1 = x+1,y
            if 0<=x1<m and 0<=y1<n: dp[y][x] += self.dfs(x1,y1,m,n)
            x2,y2 = x,y+1
            if 0<=x2<m and 0<=y2<n: dp[y][x] += self.dfs(x2,y2,m,n)
        return dp[y][x]
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        global dp
        dp = [[1e9]*n for _ in range(m)]
        answer = self.dfs(0,0,n,m)
        return answer