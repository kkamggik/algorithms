 class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0: return False
        div = [2,3,5]
        for d in div:
            while n%d==0:
                n//=d
        return n==1