def left_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]: 
            left = mid + 1
        else:
            right = mid - 1
    return left
def right_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if target >= nums[mid]: 
            left = mid + 1
        else:
            right = mid - 1
    return right
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = left_search(nums, target)
        b = right_search(nums, target)
        if a <= b: return [a,b]
        return [-1,-1]
        