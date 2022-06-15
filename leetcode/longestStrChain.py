class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def check(w1,w2):
            i1 = i2 = 0
            while i1<len(w1) and i2<len(w2):
                if w1[i1]==w2[i2]:
                    i1 += 1
                    i2 += 1
                else:
                    i2 += 1
            if i1+1 == i2 or i1==i2: return True
            return False
        words.sort(key = lambda x:len(x))
        dp = [1]*len(words)
        for i in range(1,len(words)):
            word = words[i]
            for j in range(i):
                if len(words[j])+1 == len(word) and dp[j] >= dp[i] and check(words[j],word)==True:
                    dp[i] = dp[j]+1          
        return max(dp)