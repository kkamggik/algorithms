class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for n in nums:
            if dic[n] == 1 and (n-1 not in dic) and (n+1 not in dic):
                answer.append(n)
        return answer