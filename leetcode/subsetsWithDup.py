class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums)+1):
            com = combinations(nums,i)
            for c in com: res.add(c)
        ans = []
        for r in res:
            ans.append(list(r))
        return res