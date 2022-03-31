class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        start, end = max(nums), sum(nums)
        while start <= end:
            mid = (start+end)//2
            cnt = 1
            val = nums[0]
            for i in range(1, len(nums)):
                if nums[i]+val <= mid:
                    val += nums[i]
                else:
                    cnt += 1
                    val = nums[i]
            if cnt > m:
                start = mid + 1
            else:
                end = mid - 1
        return start
        