class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(target, idx):
            if target==0:
                res.append(arr[:])
                return 
            if target < 0 or idx >= len(candidates):
                return
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                dfs(target - candidates[i], i)
                arr.pop()
        arr = []
        res = []
        dfs(target, 0)
        return res