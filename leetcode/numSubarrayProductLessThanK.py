class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        product = 1
        res = left = 0
        for idx,val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            res += idx - left + 1
        return res
            
        