class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        end = start = 0
        prev = nums[0]
        for i in range(1, n):
            if prev > nums[i]:
                end = i
            else:
                prev = nums[i]
        prev = nums[n-1]
        for i in range(n-2,-1,-1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if start==0 and end==0: return 0
        return end-start+1