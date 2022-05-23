class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic: dic[s[i]] = i
        res = -1
        for i in range(1,len(s)):
            res = max(res, i-dic[s[i]]-1)
        return res