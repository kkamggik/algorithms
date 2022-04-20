class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        n = len(s)
        if n%k != 0:
            s += fill*(k-(n%k))
        res = []
        for i in range(0,len(s),k):
            res.append(s[i:i+k])
        return res