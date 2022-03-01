class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        start,end = 0,len(matrix)-1
        while start < end:
            matrix[start],matrix[end] = matrix[end],matrix[start]
            start += 1
            end -= 1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix
            