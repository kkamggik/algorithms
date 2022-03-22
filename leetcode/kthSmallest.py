class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        start,end = matrix[0][0], matrix[n-1][n-1]
        while start <= end:
            mid = (start+end)//2
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= mid: cnt += 1
                    else: break
            if cnt < k:
                start = mid + 1
            else:
                end = mid - 1
        return start