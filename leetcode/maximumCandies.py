class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(candies)
        if s < k: return 0
        start,end = 1, s//k
        ans = 0
        while start <= end:
            mid = (start+end)//2
            cnt = 0
            for candy in candies:
                cnt += candy // mid
            if cnt >= k:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans
