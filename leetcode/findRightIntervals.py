class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        s = []
        for idx, time in enumerate(intervals):
            a,b = time
            s.append([a,b,idx])
        s.sort()
        res = []
        lst = [i for i,j,k in s]
        for a,b in intervals:
            idx = bisect.bisect_left(lst,b)
            res.append(s[idx][2] if idx<len(intervals) else -1)
        return res