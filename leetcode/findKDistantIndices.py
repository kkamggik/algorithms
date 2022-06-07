class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        stack = []
        for idx,n in enumerate(nums):
            if n==key: stack.append(idx)
        for idx,n in enumerate(nums):
            if n!=key:
                while len(stack)>=2 and abs(stack[0]-idx) > k and abs(stack[1]-idx) <= k: stack.pop(0)
                if stack and abs(stack[0]-idx) <= k:
                    res.append(idx)
            else: res.append(idx)
        return res