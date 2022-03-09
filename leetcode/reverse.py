class Solution(object):
    def reverse(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right],array[left]
            left += 1
            right -= 1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(0, len(nums)-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums)-1, nums)