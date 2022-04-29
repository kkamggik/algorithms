class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = 1
        res = 1
        for i in range(1,n):
            if nums[i-1] < nums[i]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res