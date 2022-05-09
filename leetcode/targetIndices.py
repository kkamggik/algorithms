class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        nums.sort()
        for idx,val in enumerate(nums):
            if val==target: ans.append(idx)
        return ans