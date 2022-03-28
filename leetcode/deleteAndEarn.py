class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = [0]*10001
        for n in nums:
            summ[n] += n
        for i in range(2, 10001):
            summ[i] = max(summ[i-1], summ[i-2] + summ[i])
        return summ[10000]
            