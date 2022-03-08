class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end:
            mid = (start+end)//2
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid + 1
        return end