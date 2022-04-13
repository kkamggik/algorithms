class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(grid),len(grid[0])
        if grid[0][0]==1 or grid[n-1][m-1]==1: return -1
        queue = deque()
        queue.append([0,0,1])
        visited = [[0]*m for _ in range(n)]
        dirc = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        visited[0][0] = 1
        while queue:
            x,y,c = queue.popleft()
            if x==m-1 and y==n-1: return c
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and grid[ny][nx]==0:
                    visited[ny][nx] = 1
                    queue.append([nx,ny,c+1])
        return -1
                
            
            