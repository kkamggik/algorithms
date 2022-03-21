class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                n = nums[i+1]
                if n in dic: dic[n] += 1
                else: dic[n] = 1
        maximum = 0
        target = -1
        for k,v in dic.items():
            if v > maximum:
                maximum = v
                target = k
        return target
        