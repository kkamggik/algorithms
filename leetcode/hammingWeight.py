class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        for i in range(32):
            rst += (n & 1)
            n = n >> 1
        return rst