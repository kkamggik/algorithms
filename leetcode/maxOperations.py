class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        start,end = 0,len(nums)-1
        res = 0
        while start < end:
            s = nums[start]+nums[end]
            if s==k:
                start += 1
                end -= 1
                res += 1
            elif s > k:
                end -= 1
            else:
                start += 1
        return res