class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mul = 0
        summ = sum(nums)
        for idx,val in enumerate(nums):
            mul += idx*val
        res = mul
        for i in range(1,n):
            mul += (summ-(nums[-i]*n))
            res = max(res, mul)
        return res
