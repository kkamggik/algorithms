class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # nums = list(set(nums)
        nums = [[n, i] for i, n in enumerate(nums)]
        nums.sort()
        n = len(nums)
        for i in range(0,n-1):
            start,end = i,i+1
            while end < n:
                tt = nums[end][0]-nums[start][0]
                tk = abs(nums[end][1]-nums[start][1])
                if tt <= t and tk <= k:
                    return True
                elif tt > t:
                    break
                else:
                    end += 1
        return False