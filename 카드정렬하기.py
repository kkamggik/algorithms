import heapq
n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap,int(input()))
ans = 0
while len(heap)!=1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    s = a + b
    heapq.heappush(heap, s)
    ans += s
print(ans)