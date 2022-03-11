import heapq
import sys
input = sys.stdin.readline
n = int(input())
answer = 0
heap = []
for _ in range(n):
    x = int(input())
    heapq.heappush(heap,x)
while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    answer += (x+y)
    heapq.heappush(heap, x+y)
print(answer)