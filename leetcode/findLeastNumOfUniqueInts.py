class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        counter = Counter(arr).most_common()[::-1]
        res = len(counter)
        for n,c in counter:
            if k >= c:
                k -= c
                res -= 1
            else: break
        return res
            
        