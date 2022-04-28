class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            freq = [0]*26
            for j in range(i,n):
                freq[ord(s[j])-97] += 1
                res += max(freq) - min(x for x in freq if x)
        return res
                