import heapq
arr = list(map(int, input().split()))
k = int(input())
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, [arr[i],i+1])
if sum(arr)<=k: print(-1)
else:
    total = 0
    prev = 0
    while ((heap[0][0]-prev)*len(heap)) <= k:
        k -= (heap[0][0]-prev)*len(heap)
        prev  = heap[0][0]
        heapq.heappop(heap)
    rst = sorted(heap, key = lambda x:x[1])
    print(rst[k%len(heap)][1])