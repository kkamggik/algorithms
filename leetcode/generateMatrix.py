class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        dirc = [[1,0],[0,1],[-1,0],[0,-1]]
        val = 1
        x,y,d = 0,0,0
        while True:
            res[y][x] = val
            val += 1
            nx,ny = x+dirc[d][0],y+dirc[d][1]
            if 0<=nx<n and 0<=ny<n and res[ny][nx]==0:
                x,y = nx,ny
            else:
                d = (d+1)%4
                nx,ny = x+dirc[d][0],y+dirc[d][1]
                if 0<=nx<n and 0<=ny<n and res[ny][nx]==0:
                    x,y = nx,ny
                else: break
        return res