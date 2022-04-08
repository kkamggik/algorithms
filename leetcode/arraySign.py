class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = 0
        for n in nums:
            if n==0: return 0
            elif n<0: neg += 1 
        if neg%2: return -1
        return 1