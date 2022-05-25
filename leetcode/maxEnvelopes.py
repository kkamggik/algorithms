class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        res = []
        for i, e in enumerate(envelopes):
            idx = bisect_left(res, e[1])
            if idx == len(res):
                res.append(e[1])
            else:
                res[idx]=e[1]
        return len(res)   