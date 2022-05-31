class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        res = set()
        for i in range(0,len(s)-k+1):
            res.add(s[i:i+k])
        return len(res)==2**k