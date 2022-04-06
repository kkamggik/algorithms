class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        heap = []
        for i in range(len(aliceValues)):
            heapq.heappush(heap, [-aliceValues[i]-bobValues[i],aliceValues[i],bobValues[i]])
        alice = bob = 0
        idx = 0
        while heap:
            total,a,b = heapq.heappop(heap)
            if idx % 2 == 0:
                alice += a
            else:
                bob += b
            idx += 1
        if alice == bob: return 0
        return 1 if alice > bob else -1