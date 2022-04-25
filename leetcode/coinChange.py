class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        coins = set(coins)
        if amount==0: return 0
        dp = [1e9]*(amount+1)
        dp[0] = 0
        for j in range(1,amount+1):
            for coin in coins:
                if j - coin >= 0:
                    dp[j] = min(dp[j],dp[j-coin]+1)
        return dp[amount] if dp[amount]!=1e9 else -1