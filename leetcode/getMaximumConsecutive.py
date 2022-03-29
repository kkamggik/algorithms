class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        res = 1
        for c in coins:
            if c > res:
                break
            res += c
        return res
                