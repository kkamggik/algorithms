class Solution(object):
    def binary(self, nums, start, end, target):
        if start <= end:
            mid = (start+end)//2
            if target == nums[mid]: return mid
            if target < nums[mid]: return self.binary(nums, start, mid-1, target)
            else: return self.binary(nums, mid+1, end, target)
        return -1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary(nums, 0, len(nums)-1, target)