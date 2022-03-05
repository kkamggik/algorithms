class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minval = prices[0]
        answer = 0
        for i in range(1,len(prices)):
            minval = min(minval, prices[i])
            answer = max(answer, prices[i]-minval)
        return answer