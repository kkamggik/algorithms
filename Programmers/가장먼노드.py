import heapq
def dijkstra(n,arr):
    dist = [1e9]*(n+1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap,[1,0])
    while heap:
        x,d = heapq.heappop(heap)
        if d > dist[x]: continue
        for idx in arr[x]:
            if d+1 < dist[idx]:
                dist[idx] = d+1
                heapq.heappush(heap,[idx,dist[idx]])
    return dist
    
def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n+1)]
    for a,b in edge:
        arr[a].append(b)
        arr[b].append(a)
    dist = dijkstra(n,arr)
    print(dist)
    return dist.count(max(dist[1:]))
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))