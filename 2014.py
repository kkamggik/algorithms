import heapq
k,n = map(int, input().split())
arr = list(map(int, input().split()))
heap = []
for num in arr: heapq.heappush(heap, num)
for i in range(n):
    num = heapq.heappop(num)
    for j in range(n):
        num