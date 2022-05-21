class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res = 1e9
        ans = []
        arr.sort()
        for i in range(1,len(arr)):
            d = arr[i]-arr[i-1]
            if d < res:
                res = d
                ans = [[arr[i-1],arr[i]]]
            elif d == res:
                ans.append([arr[i-1],arr[i]])
        return ans