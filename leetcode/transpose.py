class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m = len(matrix),len(matrix[0])
        rst =[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rst[i][j] = matrix[j][i]
        return rst