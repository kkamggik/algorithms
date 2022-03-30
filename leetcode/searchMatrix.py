class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n,m = len(matrix), len(matrix[0])
        start, end = 0, n*m-1
        while start <= end:
            mid = (start+end)//2
            mr,mc = mid//m, mid%m
            if matrix[mr][mc] == target: return True
            if matrix[mr][mc] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
        
        