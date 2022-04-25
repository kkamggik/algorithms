class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2 or n==3: return n-1
        three = 1
        while n > 4:
            n -= 3
            three *= 3
        return three*n
        