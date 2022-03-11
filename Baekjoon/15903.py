import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
heap = []
arr = list(map(int, input().split()))
for num in arr: heapq.heappush(heap, num)
for i in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    heapq.heappush(heap, x+y)
answer = 0
while heap:
    answer += heapq.heappop(heap)
print(answer)