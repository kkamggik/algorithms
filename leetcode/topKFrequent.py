class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n not in dic: dic[n] = 1
            else: dic[n] += 1 
        freq = [[] for _ in range(len(nums)+1)]
        for key,val in dic.items():
            freq[val].append(key)
        res = []
        for lst in freq[::-1]:
            for i in range(len(lst)):
                res.append(lst[i])
        return res[:k]