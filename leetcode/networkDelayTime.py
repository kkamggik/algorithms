class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [[] for _ in range(n+1)]
        for a,b,c in times:
            arr[a].append([b,c])
        def dijkstra(v):
            dist = [1e9]*(n+1)
            dist[v] = 0
            heap = []
            heapq.heappush(heap, [v,0])
            while heap:
                v,d = heapq.heappop(heap)
                if dist[v] < d: continue
                for nxt,nd in arr[v]:
                    if d+nd < dist[nxt]:
                        dist[nxt] = d+nd
                        heapq.heappush(heap,[nxt,dist[nxt]])
            if 1e9 in dist[1:]: return -1
            return max(dist[1:])
        return dijkstra(k)