class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        for i,n in enumerate(nums):
            heapq.heappush(heap,[n,i])
        rem = len(nums)-k
        for i in range(rem):
            heapq.heappop(heap)
        res = []
        while heap:
            n,i = heapq.heappop(heap)
            res.append([i,n])
        res.sort(key=lambda x:x[0])
        ans = []
        for i,n in res: ans.append(n)
        return ans