class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]: answer += 1
        return answer