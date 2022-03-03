class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        zero = []
        m = len(matrix[0])
        n = len(matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: 
                    zero.append([j,i])
        for x,y in zero:
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                while 0<=nx<m and 0<=ny<n:
                    matrix[ny][nx] = 0
                    nx,ny = nx+d[0],ny+d[1]        