class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = neg = res = 0
        for n in nums:
            if n == 0:
                pos = neg = 0
            elif n > 0:
                pos += 1
                if neg != 0: neg += 1
            else:
                t = neg
                neg = pos + 1
                if t > 0: pos = t + 1
                else: pos = 0
            res = max(res, pos)
            print(pos,neg)
        return res