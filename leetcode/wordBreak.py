class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for word in wordDict:
                if dp[i-len(word)]==True and s[i-len(word):i]==word:
                    dp[i] = True
        return dp[-1]