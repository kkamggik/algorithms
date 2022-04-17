class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        res = 1e9
        dp = [1e9] * len(arr)
        i = curr = 0
        for j,n in enumerate(arr):
            curr += n
            while curr > target:
                curr -= arr[i]
                i += 1
            if target == curr:
                start = j - i + 1
                res = min(res, start + dp[i-1])
                dp[j] = min(start, dp[j-1])
            else:
                dp[j] = dp[j-1]
        return res if res!=1e9 else -1
s = Solution()
s.minSumOfLengths([7,3,4,7], 7)
