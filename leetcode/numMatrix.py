class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.mat = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.mat[i+1][j+1] = self.mat[i+1][j] + self.mat[i][j+1] - self.mat[i][j] + self.matrix[i][j]
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.mat[row2+1][col2+1] - self.mat[row1][col2+1] - self.mat[row2+1][col1] + self.mat[row1][col1]
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)