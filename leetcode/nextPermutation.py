class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1,i,-1):
                    if nums[j] > nums[i]:
                        nums[i],nums[j] = nums[j],nums[i]
                        start = i+1
                        end = len(nums)-1
                        mid = (start+end)//2
                        for k in range(start,mid+1):
                            nums[k],nums[end] = nums[end],nums[k]
                            end -= 1
                        return
        start,end = 0,len(nums)-1
        mid = (start+end)//2
        for i in range(mid+1):
            nums[i],nums[end] = nums[end],nums[i]
            end -= 1
        return