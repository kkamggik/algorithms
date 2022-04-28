class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        n,m = len(heights),len(heights[0])
        heap = []
        heapq.heappush(heap,[0,0,0])
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        res = 0
        while heap:
            c,x,y = heapq.heappop(heap)
            visited.add((x,y))
            res = max(res, c)
            if x==m-1 and y==n-1:
                return res
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                    heapq.heappush(heap,[abs(heights[ny][nx]-heights[y][x]),nx,ny])
        return res