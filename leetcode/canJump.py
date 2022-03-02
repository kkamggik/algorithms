class Solution(object):
    def canJump(self, nums):
        m = 0
        for idx, val in enumerate(nums):
            if idx > m:
                return False
            m = max(m, idx+val)
        return True