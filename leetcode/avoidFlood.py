class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        res = [-1]*len(rains)
        for idx,lake in enumerate(rains):
            dic[lake].append(idx)
        full = set()
        empty = []
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if lake in full: return []
                full.add(lake)
                dic[lake].pop(0)
                if dic[lake]:
                    heapq.heappush(empty, dic[lake][0])
            else:
                if empty:
                    res[i] = rains[heapq.heappop(empty)]
                    full.remove(res[i])
                else:
                    res[i] = 1
        return res
                