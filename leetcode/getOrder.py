class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        for i in range(len(tasks)):
            t = tasks[i]
            heapq.heappush(heap,[t[0],t[1],i])
        poss = []
        res = []
        time = 0
        while heap:
            if not poss and time < heap[0][0]:
                time = heap[0][0]
            else:
                while heap and heap[0][0] <= time:
                    e,p,i = heapq.heappop(heap)
                    heapq.heappush(poss,[p,i])
                p,i = heapq.heappop(poss)
                time += p
                res.append(i)
        while poss:
            p,i = heapq.heappop(poss)
            res.append(i)
        return res