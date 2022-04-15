class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(target, idx):
            if target==0:
                res.append(arr[:])
                print(arr)
                return 
            if target < 0 or idx >= len(candidates):
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i]==candidates[i-1]: continue
                arr.append(candidates[i])
                dfs(target - candidates[i], i+1)
                arr.pop()
        arr = []
        res = []
        candidates.sort()
        dfs(target, 0)
        return res