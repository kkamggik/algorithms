class Solution(object):
    def dfs(self, idx, arr, nums):
        global res
        if(len(arr) > 1):
            res.add((tuple(arr[:])))
        for i in range(idx, len(nums)):
            if not arr or arr[-1] <= nums[i]:
                self.dfs(i+1,arr+[nums[i]],nums)
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global visited, res
        res = set()
        self.dfs(0,[],nums)
        return res