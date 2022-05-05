class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        res = 0
        for row in mat:
            res += min(row)
        if res >= target: return res-target
        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums if x + i <= 2 * target - res}
        return min(abs(x-target) for x in nums)
