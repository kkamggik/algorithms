class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        res = summ = 0
        # sort efficiencies in descending order
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(heap,s)
            summ += s
            if len(heap) > k:
                summ -= heapq.heappop(heap)
            # 어차피 지금 e 가 지금까지중에 제일 작은 e임!
            res = max(res, summ*e)
        return res%(10**9 + 7)