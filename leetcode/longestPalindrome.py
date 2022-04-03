class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            if c not in dic: dic[c] = 1
            else: dic[c] += 1
        res = odd = 0
        for k,v in dic.items():
            res += (v//2)*2
            if v%2: odd = 1
        return res+odd