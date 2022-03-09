class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] >= 0: break
        pos = i
        neg = i-1
        answer = []
        while neg >= 0 or pos < len(nums):
            if neg >= 0 and pos < len(nums):
                n1 = nums[neg]**2
                n2 = nums[pos]**2
                if n1 < n2:
                    answer.append(n1)
                    neg -= 1
                else:
                    answer.append(n2)
                    pos += 1
            elif neg < 0:
                answer.append(nums[pos]**2)
                pos += 1
            else:
                answer.append(nums[neg]**2)
                neg -= 1
        return answer