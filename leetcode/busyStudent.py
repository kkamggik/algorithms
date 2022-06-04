class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        student = [0]*1002
        for s in startTime:
            student[s] += 1
        for e in endTime:
            student[e+1] -= 1
        res = 0
        for i in range(queryTime+1):
            res += student[i]
        return res
        