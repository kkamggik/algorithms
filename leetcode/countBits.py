class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]
        while len(dp) <= n:
            dp += [i+1 for i in dp]
        return dp[:n+1]