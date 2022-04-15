class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [0]*len(nums)
        arr = []
        def permutation(cnt):
            if cnt==len(visited):
                res.add(tuple(arr[:]))
                return
            for i in range(len(nums)):
                if visited[i]==0:
                    visited[i] = 1
                    arr.append(nums[i])
                    permutation(cnt+1)
                    arr.pop()
                    visited[i] = 0
        res = set()
        permutation(0)
        return res