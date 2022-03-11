import heapq
import sys
input = sys.stdin.readline
n = int(input())
greater, less = [],[]
for _ in range(n):
    x = int(input())
    if len(greater) == len(less):
        heapq.heappush(greater, -x)
    else:
        heapq.heappush(less, x)
    if greater and less and -greater[0] > less[0]:
        g = -heapq.heappop(greater)
        l = heapq.heappop(less)
        heapq.heappush(greater, -l)
        heapq.heappush(less, g)
    if len(greater) != len(less): print(-greater[0])
    else: print(min(-greater[0], less[0]))
