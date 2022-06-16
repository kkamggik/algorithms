class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start,end = 0,50000
        while start <= end:
            val = start**2 + end**2
            if val == c: return True
            if val > c:
                end -= 1
            else:
                start += 1
        return False