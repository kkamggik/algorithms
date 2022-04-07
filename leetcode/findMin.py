class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,len(nums)-1
        while nums[start] > nums[end]:
            mid = (start+end)//2
            if nums[start] <= nums[mid]:
                start = mid+1
            else:
                end = mid
        return nums[start]
            
                