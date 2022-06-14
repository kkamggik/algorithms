class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights: return []
        pacific = set()
        atlantic = set()
        m,n = len(heights[0]),len(heights)
        def dfs(x,y,s):
            s.add((y,x))
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and heights[ny][nx] >= heights[y][x] and (ny,nx) not in s:
                    dfs(nx,ny,s)
        for i in range(n):
            dfs(0,i,pacific)
            dfs(m-1,i,atlantic)
        for j in range(m):
            dfs(j,0,pacific)
            dfs(j,n-1,atlantic)
        return list(pacific & atlantic)