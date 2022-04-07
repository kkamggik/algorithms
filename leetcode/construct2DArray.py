class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        n,m = m,n
        if len(original) != n*m: return []
        res = [[0]*m for _ in range(n)]
        row = 0
        for i in range(len(original)):
            if i!=0 and i%m==0:
                row += 1
            res[row][i%m] = original[i]
        return res
            