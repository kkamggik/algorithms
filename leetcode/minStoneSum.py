class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for p in piles:
            heapq.heappush(heap, -p)
        for i in range(k):
            x = -heapq.heappop(heap)
            x = x//2 if x%2==0 else (x//2)+1
            heapq.heappush(heap, -x)
        res = 0
        while heap:
            res += -(heapq.heappop(heap))
        return res