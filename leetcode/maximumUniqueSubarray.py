class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = cnt = res = 0
        summ = 0
        dic = defaultdict(int)
        while end < len(nums):
            n = nums[end]
            if dic[n] == 0:
                cnt += 1
                end += 1
                dic[n] = 1
                summ += n
                res = max(res, summ)
            else:
                s = nums[start]
                dic[s] = 0
                cnt -= 1
                start += 1
                summ -= s
        return res