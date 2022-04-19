class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        n1 = set(nums1)
        n2 = set(nums2)
        for n in n1:
            if n in n2:
                res.append(n)
        return res