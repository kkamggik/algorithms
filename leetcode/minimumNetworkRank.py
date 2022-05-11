class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        res = 0
        arr = [[] for _ in range(n)]
        for a,b in roads:
            arr[a].append(b)
            arr[b].append(a)
        for i in range(n-1):
            for j in range(i+1,n):
                res = max(res, len(arr[i]) + len(arr[j]) -1 if i in arr[j] else len(arr[i]) + len(arr[j]))
        return res