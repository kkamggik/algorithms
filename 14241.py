import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
heap = []
answer = 0
for a in arr:
    heapq.heappush(heap, -a)
while len(heap) > 1:
    x = -heapq.heappop(heap)
    y = -heapq.heappop(heap)
    answer += x*y
    heapq.heappush(heap, -(x+y))
print(answer)