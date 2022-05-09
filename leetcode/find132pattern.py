class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2: return False
        left = [1e9]*n
        left[0] = nums[0]
        for i in range(1,n):
            left[i] = min(left[i-1], nums[i])
        stack = []
        for i in range(n-1,-1,-1):
            if left[i] < nums[i]:
                while stack and stack[-1] <= left[i]: stack.pop()
                if stack and left[i] < stack[-1] < nums[i]: return True
            stack.append(nums[i])
        return False