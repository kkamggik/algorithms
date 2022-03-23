class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        cnt = 0
        while target > startValue:
            if target%2==1:
                target += 1
            else:
                target //= 2
            cnt += 1
        return cnt + startValue - target