class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m = len(mat), len(mat[0])
        for i in range(n-1,-1,-1):
            x,y = 0,i
            stack = []
            while x<m and y<n:
                stack.append(mat[y][x])
                x += 1
                y += 1
            stack.sort()
            x,y = 0,i
            while x<m and y<n:
                mat[y][x] = stack.pop(0)
                x += 1
                y += 1
        for i in range(1,m):
            x,y = i,0
            stack = []
            while x<m and y<n:
                stack.append(mat[y][x])
                x += 1
                y += 1
            stack.sort()
            x,y = i,0
            while x<m and y<n:
                v = stack.pop(0)
                mat[y][x] = v
                x += 1
                y += 1
        return mat