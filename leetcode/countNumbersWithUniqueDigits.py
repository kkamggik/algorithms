class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 1
        ans, val = 10, 9
        for i in range(1,n):
            val *= (10-i)
            ans += val
        return ans