class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        p = [i for i in range(len(s)) if s[i] == '|']
        res = []
        for a,b in queries:
            l = bisect.bisect_left(p,a)
            r = bisect.bisect_right(p,b)
            res.append(p[r-1] - p[l] - (r-1-l) if r > l else 0)
        return res