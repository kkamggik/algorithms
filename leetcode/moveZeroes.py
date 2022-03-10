class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0,0
        while right < len(nums):
            if nums[left]!=0:
                left += 1
                right += 1
            elif nums[left]==0 and nums[right]!=0:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1                