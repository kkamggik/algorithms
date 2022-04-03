class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = set()
        for c in s:
            if c.isdigit(): lst.add(c)
        res = []
        for c in lst: res.append(c)
        if len(res)<=1: return -1
        res.sort()
        return res[-2]