class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = cnt = end = 0
        for i in range(len(nums)-1):
            curr = max(curr, i+nums[i])
            if i == end:
                cnt += 1
                end = curr
        print(cnt)
s = Solution()
s.jump([2,3,1,1,4])