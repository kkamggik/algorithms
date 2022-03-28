class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start,end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target: return True
            elif nums[mid] == nums[end]: end -= 1
            elif nums[mid] > nums[end]:
                if nums[start] <= target and target < nums[mid]: end = mid - 1
                else: start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]: start = mid + 1
                else: end = mid - 1
        return False