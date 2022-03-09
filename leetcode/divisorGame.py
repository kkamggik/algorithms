class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        cnt = 0
        while n > 1:
            if n % x == 0:
                n -= x
                cnt += 1
        if cnt % 2 == 0: return False
        return True
        