class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,-(x-y))
        if not heap: return 0
        return -heapq.heappop(heap)
            