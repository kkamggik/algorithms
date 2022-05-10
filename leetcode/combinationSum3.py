class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(idx,arr):
            if sum(arr)>=n:
                if sum(arr)==n and len(arr)==k:
                    answer.append(arr[:])
                return
            for i in range(idx,len(nums)):
                if visited[i]==0:
                    visited[i] = 1
                    arr.append(nums[i])
                    dfs(i+1, arr)
                    arr.pop()
                    visited[i] = 0
        nums = [i for i in range(1,10)]
        answer = []
        visited = [0]*10
        dfs(0,[])
        return answer