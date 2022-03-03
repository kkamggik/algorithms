from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = set()
        for i in range(len(nums)+1):
            com = combinations(nums,i)
            for c in com: answer.add(c)
        rst = []
        for ans in answer:
            a = list(ans)
            rst.append(a)
        return rst