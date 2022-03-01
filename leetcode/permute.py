class Solution(object):
    def dfs(self, idx, array, nums):
        if len(array)==len(nums):
            global answer
            arr = [item for item in array]
            answer.append(arr)
            return
        global visited
        for i in range(len(nums)):
            if visited[i]==0:
                visited[i] = 1
                array.append(nums[i])
                self.dfs(idx+1, array, nums)
                array.pop()
                visited[i] = 0
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global visited, answer
        answer = []
        visited = [0]*len(nums)
        self.dfs(0, [], nums)
        return answer