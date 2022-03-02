class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        answer = []
        for x,y in intervals[1:]:
            if end >= x:
                end = max(end,y)
            else:
                answer.append([start,end])
                start = x
                end = y
        answer.append([start,end])
        return answer