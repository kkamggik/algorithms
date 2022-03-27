class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(mat)):
            s = mat[i].count(1)
            res.append([s,i])
        res.sort()
        rst = []
        for i in range(k):
            rst.append(res[i][1])
        return rst