class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(changed)
        if counter[0] % 2:
            return []
        for x in sorted(counter):
            if counter[x] > counter[2 * x]:
                return [] 
            if x!=0:
                counter[2 * x] -= counter[x]
            else:
                counter[x] //= 2
        return list(counter.elements())