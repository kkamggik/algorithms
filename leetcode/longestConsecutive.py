class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = set(nums)
        answer = 0
        for n in numbers:
            if n-1 in numbers: continue
            cnt = 1
            curr = n+1
            while curr in numbers:
                curr += 1
                cnt += 1
            answer = max(answer, cnt)
        return answer