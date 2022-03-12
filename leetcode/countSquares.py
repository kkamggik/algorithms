class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!=0: matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
        answer = 0
        for i in range(n):
            for j in range(m):
                answer += matrix[i][j]
        return answer