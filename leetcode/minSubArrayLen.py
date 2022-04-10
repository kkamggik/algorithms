class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        summ = start = 0
        res = 1e9
        for end in range(len(nums)):
            summ += nums[end]
            while summ >= target:
                res = min(res, end-start+1)
                summ -= nums[start]
                start += 1
        return res if res!=1e9 else 0