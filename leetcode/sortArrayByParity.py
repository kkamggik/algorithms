class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0]*n
        idx = 0
        for num in nums:
            if num%2==0:
                res[idx] = num
                idx += 1
        for num in nums:
            if num%2==1:
                res[idx] = num
                idx += 1
        return res