class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n = len(security)
        if time==0: return [i for i in range(n)]
        increasing = [0]*n
        decreasing = [0]*n
        for i in range(1,n):
            if security[i] >= security[i-1]:
                increasing[i] = increasing[i-1]+1
        for i in range(n-2,-1,-1):
            if security[i] >= security[i+1]:
                decreasing[i] = decreasing[i+1]+1
        res = []
        print(increasing)
        print(decreasing)
        for i in range(time,n-time):
            if increasing[i+time]>=time and decreasing[i-time]>=time:
                res.append(i)
        return res