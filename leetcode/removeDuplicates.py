class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        current_smallest = nums[0]
        for i in range(1,len(nums)):
            if current_smallest < nums[i]:
                nums[idx] = nums[i]
                idx += 1
                current_smallest = nums[i]
        return idx